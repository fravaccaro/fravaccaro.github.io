#!/usr/bin/env python3
"""Light proofreading pass over imported blog posts."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

# (pattern, replacement) — applied to body + title lines only, after front matter
REPLACEMENTS = [
    # Titles / bodies — misspellings & grammar
    ("Announched", "Announced"),
    ("&amp;", "&"),
    ("Let me introduce you Jolla", "Let me introduce you to Jolla"),
    ("before import them", "before importing them"),
    ("meetups sum up", "meetups summary"),
    ("Qwerty", "QWERTY"),
    ("Whatsapp", "WhatsApp"),
    ("ispired", "inspired"),
    ("31th", "31st"),
    ("cutted", "cut"),
    ("simply but", "simple but"),
    ("it automatically set your phone", "it automatically sets your phone"),
    ("it automatically set ", "it automatically sets "),
    ("give an hand", "give a hand"),
    ("informations", "information"),
    ("as usually", "as usual"),
    ("subjected to changes", "subject to change"),
    ("should works", "should work"),
    ("some occasionally delays", "occasional delays"),
    ("Did you noticed", "Did you notice"),
    ("lacks of", "lacks"),
    ("give an hint", "give a hint"),
    ("more infos", "more info"),
    ("organic thought", "organic thoughts"),
    ("comfortable to use it as a blog", "comfortable to use as a blog"),
    ("non so IT-skilled", "not so IT-skilled"),
    ("do they worth", "are they worth"),
    ("NSA-affaire", "NSA affair"),
    # Italian
    ("Dirò nvece", "Dirò invece"),
    ("vi consiglio la ormai classica", "vi consiglio l'ormai classica"),
]

YOUTUBE_RE = re.compile(
    r"\[youtube\s+(https?://(?:www\.)?youtube\.com/watch\?v=([^\s\]?]+)[^\]]*)\]",
    re.IGNORECASE,
)
GALLERY_RE = re.compile(r'\[gallery[^\]]*\]', re.IGNORECASE)
AUTOLINK_RE = re.compile(r"\(<(https?://[^>]+)>\)")
FLICKR_LINK_RE = re.compile(r"\(<(https?://[^>]+)>\s*(\"[^\"]*\")?\)")


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    fm = text[: end + 5]
    body = text[end + 5 :]
    return fm, body


def fix_youtube(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        vid = m.group(2).split("?")[0]
        return f"[YouTube video](https://www.youtube.com/watch?v={vid})"

    return YOUTUBE_RE.sub(repl, text)


def fix_autolinks(text: str) -> str:
    text = FLICKR_LINK_RE.sub(lambda m: f"({m.group(1)}{m.group(2) or ''})", text)
    return AUTOLINK_RE.sub(r"(\1)", text)


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(original)
    if not fm:
        return False

    for old, new in REPLACEMENTS:
        fm = fm.replace(old, new)
        body = body.replace(old, new)
    body = fix_youtube(fix_autolinks(body))
    body = GALLERY_RE.sub("<!-- gallery omitted -->", body)
    changed = fm + body

    if changed != original:
        path.write_text(changed, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = []
    for path in sorted(POSTS.rglob("*.md")):
        if process_file(path):
            updated.append(path.relative_to(ROOT))
    print(f"Updated {len(updated)} posts:")
    for p in updated:
        print(f"  {p}")


if __name__ == "__main__":
    main()
