#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = 'Ron'
SITENAME = "My Pelican Test Blog"
SITEURL = SITEURL_ROOT + '/blog/en'
DEFAULT_LANG = 'en'
MENUITEMS = (
            ('Chinese Blog（中文博客）', SITEURL_ROOT + '/blog/zh'),
            )
DISPLAY_PAGES_ON_MENU = True
