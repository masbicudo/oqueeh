@echo off
echo.source 'https://rubygems.org'>Gemfile
echo.gem 'github-pages', group: :jekyll_plugins>>Gemfile
call bundle add webrick
call bundle add wdm
call bundle install
