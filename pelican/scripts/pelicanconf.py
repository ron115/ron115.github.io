#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rongcheng Li'
SITENAME = "Rongcheng's Blog"
#SITEURL = 'http://assert-false.com/blog/en'
SITEURL = 'http://localhost:8000/blog/en'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'

PLUGIN_PATH = 'plugins'
PLUGINS = ['tipue_search']

THEME = 'themes/pelican-elegant-1.3'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search',)

#DIRECT_TEMPLATES = ('search',)

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (
#        ('Reddit Programming', 'http://www.reddit.com/r/programming/'),
#        ('YCombinator News', 'https://news.ycombinator.com/'),
#        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
