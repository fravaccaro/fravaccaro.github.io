#!/usr/bin/env python3
"""Import published WordPress posts from a WXR export into Jekyll (Moonwalk)."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

import html2text
import requests

ROOT = Path(__file__).resolve().parents[1]
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}

IMAGE_URL_RE = re.compile(
    r"https?://(?:[\w.-]+\.)?(?:wordpress\.com|wp\.com)[^\s\"'<>)]+\.(?:jpe?g|png|gif|webp)(?:\?[^\s\"'<>)]*)?",
    re.IGNORECASE,
)
IMG_SRC_RE = re.compile(r"""<img[^>]+src=["']([^"']+)["']""", re.IGNORECASE)


def wp_text(parent: ET.Element, tag: str) -> str:
    elem = parent.find(f"wp:{tag}", NS)
    if elem is None or elem.text is None:
        return ""
    return elem.text.strip()


def item_text(parent: ET.Element, tag: str, ns_key: str = "content") -> str:
    elem = parent.find(f"{ns_key}:{tag}", NS)
    if elem is None or elem.text is None:
        return ""
    return elem.text


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    inner = ", ".join(yaml_quote(v) for v in values)
    return f"[{inner}]"


def slugify_filename(name: str) -> str:
    name = unquote(name)
    name = Path(name).name.split("?")[0]
    name = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-").lower()
    return name or "image"


def collect_tags(item: ET.Element) -> list[str]:
    tags: list[str] = []
    for cat in item.findall("category"):
        domain = cat.attrib.get("domain", "")
        if domain not in {"category", "post_tag"}:
            continue
        label = (cat.text or "").strip()
        if label and label not in tags:
            tags.append(label)
    return tags


def find_image_urls(html_content: str) -> list[str]:
    urls = set(IMAGE_URL_RE.findall(html_content))
    for match in IMG_SRC_RE.findall(html_content):
        if "wordpress.com" in match or "wp.com" in match or "wp-content" in match:
            urls.add(match)
    return sorted(urls)


def download_image(
    session: requests.Session,
    url: str,
    dest_dir: Path,
    slug: str,
    used_names: set[str],
) -> str | None:
    try:
        response = session.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"  ! image failed: {url} ({exc})", file=sys.stderr)
        return None

    base = slugify_filename(urlparse(url).path)
    stem = Path(base).stem
    suffix = Path(base).suffix or ".jpg"
    candidate = f"{slug}-{stem}{suffix}"[:120]
    counter = 1
    while candidate in used_names:
        candidate = f"{slug}-{stem}-{counter}{suffix}"[:120]
        counter += 1
    used_names.add(candidate)

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / candidate
    dest.write_bytes(response.content)

    year_month = dest_dir.relative_to(ROOT / "assets" / "posts")
    return f"/assets/posts/{year_month.as_posix()}/{candidate}"


def rewrite_image_urls(content: str, mapping: dict[str, str]) -> str:
    updated = content
    for original, local in sorted(mapping.items(), key=lambda pair: len(pair[0]), reverse=True):
        updated = updated.replace(original, local)
    return updated


def html_to_markdown(html_content: str) -> str:
    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_images = False
    converter.ignore_links = False
    converter.protect_links = True
    converter.single_line_break = False
    converter.wrap_links = False
    markdown = converter.handle(html_content or "").strip()
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown


def build_link_post_body(title: str, link: str) -> str:
    return f"{title}\n\n[Read on WordPress]({link})"


def import_posts(input_path: Path, dry_run: bool = False) -> None:
    tree = ET.parse(input_path)
    channel = tree.getroot().find("channel")
    if channel is None:
        raise SystemExit("Invalid WXR: missing channel element")

    session = requests.Session()
    session.headers.update({"User-Agent": "fravaccaro-jekyll-import/1.0"})

    posts_written = 0
    images_downloaded = 0
    skipped = 0

    for item in channel.findall("item"):
        if wp_text(item, "post_type") != "post":
            continue
        if wp_text(item, "status") != "publish":
            continue

        title = (item.findtext("title") or "").strip()
        slug = wp_text(item, "post_name") or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        post_date = wp_text(item, "post_date")
        if not post_date:
            skipped += 1
            continue

        date_part = post_date[:10]
        year, month, _day = date_part.split("-")
        link = (item.findtext("link") or "").strip()
        html_content = item_text(item, "encoded", "content")
        tags = collect_tags(item)

        post_dir = ROOT / "_posts" / year / month
        assets_dir = ROOT / "assets" / "posts" / year / month
        post_file = post_dir / f"{date_part}-{slug}.md"

        image_mapping: dict[str, str] = {}
        used_names: set[str] = set()
        for url in find_image_urls(html_content):
            if dry_run:
                continue
            local_path = download_image(session, url, assets_dir, slug, used_names)
            if local_path:
                image_mapping[url] = local_path
                images_downloaded += 1

        html_content = rewrite_image_urls(html_content, image_mapping)
        markdown = html_to_markdown(html_content)
        if not markdown.strip():
            markdown = build_link_post_body(title, link)

        markdown = rewrite_image_urls(markdown, image_mapping)

        front_matter = "\n".join(
            [
                "---",
                "layout: post",
                f"title: {yaml_quote(title)}",
                f"date: {post_date} +0000",
                f"tags: {yaml_list(tags)}",
                "---",
                "",
            ]
        )
        body = front_matter + markdown + "\n"

        if dry_run:
            print(f"Would write {post_file.relative_to(ROOT)} ({len(markdown)} chars, {len(image_mapping)} images)")
        else:
            post_dir.mkdir(parents=True, exist_ok=True)
            post_file.write_text(body, encoding="utf-8")
            print(f"Wrote {post_file.relative_to(ROOT)}")
        posts_written += 1

    print(
        f"\nDone: {posts_written} posts, {images_downloaded} images downloaded, {skipped} skipped."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=ROOT / "_import" / "wordpress.xml",
        help="Path to WordPress WXR export",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    import_posts(args.input, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
