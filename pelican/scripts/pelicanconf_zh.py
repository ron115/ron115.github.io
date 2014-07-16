#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

THEME = 'themes/pelican-octopress-theme'
#THEME = 'themes/pelican-elegant-1.3'
#THEME = 'themes/gum'

AUTHOR = '李某'
SITENAME = "Pelican测试"
SITEURL = SITEURL_ROOT + '/articles-zh'
DEFAULT_LANG = 'zh_cn'
MENUITEMS = (
            ('English (英文)', SITEURL_ROOT + '/articles-en'),
            )
DISPLAY_PAGES_ON_MENU = True
