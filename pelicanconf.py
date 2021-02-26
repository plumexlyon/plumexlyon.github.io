#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "PlumeX collaboration"
SITENAME = "Plateforme PlumeX"
SITEURL = "https://plumexlyon.github.io"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Pelican", "https://getpelican.com/"),)

# Social widget
SOCIAL = tuple()
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ["img", "pdf", "pages/img"]

PLUGINS = ["pelican_bib"]
PUBLICATIONS_SRC = "content/pubs.bib"
THEME = "themes/pelican-themes/blue-penguin"
THEME_TEMPLATES_OVERRIDES = ["templates"]
DISPLAY_HOME = False
