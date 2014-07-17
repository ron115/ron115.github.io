#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

#THEME = 'themes/pelican-octopress-theme'
#THEME = 'themes/pelican-elegant-1.3'
THEME = 'themes/gum'

AUTHOR = 'Ron'
SITENAME = "My Site"
#SITEURL = SITEURL_ROOT + '/articles-en'
SITEURL = SITEURL_EN
DEFAULT_LANG = 'en'
MENUITEMS = (
            #('Chinese (中文)', SITEURL_ROOT + '/articles-zh'),
            ('中文 (Chinese)', SITEURL_ZH),
            )
DISPLAY_PAGES_ON_MENU = True
