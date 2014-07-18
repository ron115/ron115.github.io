#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# RL defined variables
#===========================================================================

# NOTE: 
# SITEURL_ROOT must set to an absolute domain URL, otherwise the pelican's
# varialbe "SITEURL" will be invalid for DISQUS with error message like: 
#
#   We were unable to load Disqus. If you are a moderator please see our
#   troubleshooting guide.
# 
# If not use DISQUS, it's OK to just set: SITEURL_ROOT = ''

#SITEURL_ROOT = 'http://localhost:8000'         # for debug
SITEURL_ROOT = 'http://assert-false.com'        # for publish

SITEURL_EN = SITEURL_ROOT + '/en'
SITEURL_ZH = SITEURL_ROOT + '/zh'

#===========================================================================

TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10


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

