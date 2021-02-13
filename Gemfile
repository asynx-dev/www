source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 4.2.0"
# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.5"
# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins
# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-last-modified-at"
  gem 'jekyll-archives'
  gem 'classifier-reborn'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# We are modifying some template files in the repo so fix the version and
# change it manually
gem "minimal-mistakes-jekyll", "4.22.0"
gem "html-proofer"

# See: https://stackoverflow.com/a/65547010/1766391
# This is needed for serve --livereload on Windows
gem 'eventmachine', '1.2.7', git: 'https://github.com/eventmachine/eventmachine.git', tag: 'v1.2.7', :platforms => [:mingw, :x64_mingw, :mswin]
