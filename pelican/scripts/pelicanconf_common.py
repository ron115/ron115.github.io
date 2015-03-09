#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True


DISQUS_SITENAME = 'ron115'


#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search',)


# Blogroll
#LINKS = (
#        ('Reddit Programming', 'http://www.reddit.com/r/programming/'),
#        ('YCombinator News', 'https://news.ycombinator.com/'),
#        )


# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


# Plugin Config
#===========================================================================
#PLUGIN_PATH = 'plugins'
#PLUGINS = ['tipue_search']


# ATOM Config
#===========================================================================
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None


# Theme config
# =========================================================================================
#THEME = 'themes/pelican-octopress-theme'
#THEME = 'themes/gum'
THEME = 'themes/pelican-elegant-1.3'

# configurations for pelican elegant theme
# see: http://oncrashreboot.com/elegant-best-pelican-theme-features#configuration-variables
# -----------------------------------------------------------------------------------------
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']

# configuration for plugin 'sitemap'
# see: https://github.com/getpelican/pelican-plugins/tree/master/sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# =========================================================================================
