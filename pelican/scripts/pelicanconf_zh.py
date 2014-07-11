#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = '李某'
SITENAME = "Pelican博客测试"
SITEURL = SITEURL_ROOT + '/article/zh'
DEFAULT_LANG = 'zh_cn'
MENUITEMS = (
            ('English Blog（英文博客）', SITEURL_ROOT + '/article/en'),
            )
DISPLAY_PAGES_ON_MENU = True
