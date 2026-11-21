# frozen_string_literal: true

source "https://rubygems.org"

gem "jekyll", "~> 4.3.4"
gem "jekyll-remote-theme"

# Jekyll 4.3 and safe_yaml load these from stdlib. Ruby 3.4+ ships them as separate gems.
gem "base64"
gem "csv"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-paginate-v2"
  gem "jekyll-sitemap"
  gem "jekyll-soopr-seo-tag", "~> 2.7"
  gem "jekyll-markdown-output", "~> 0.1"
  gem "jekyll-llms-output", "~> 0.1"
end

gem "webrick", "~> 1.8"
gem "wdm", ">= 0.1.0" if Gem.win_platform?
