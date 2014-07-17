#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

#THEME = 'themes/pelican-octopress-theme'
THEME = 'themes/pelican-elegant-1.3'
#THEME = 'themes/gum'

# configurations for pelican elegant theme
# see: http://oncrashreboot.com/elegant-best-pelican-theme-features#configuration-variables
# =========================================================================================

PLUGIN_PATH = 'plugins'
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
AUTHOR = '李某'
SITENAME = "Pelican测试"
#SITEURL = SITEURL_ROOT + '/articles-zh'
SITEURL = SITEURL_ZH
DEFAULT_LANG = 'zh_cn'
MENUITEMS = (
            #('English (英文)', SITEURL_ROOT + '/articles-en'),
            ('English (英文)', SITEURL_EN),
            )
DISPLAY_PAGES_ON_MENU = True
