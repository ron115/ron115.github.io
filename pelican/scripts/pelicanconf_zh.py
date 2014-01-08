#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = '李某'
SITENAME = "李某的博客"
SITEURL = SITEURL_ROOT + '/blog/zh'
DEFAULT_LANG = 'zh_cn'
MENUITEMS = (
            ('English Blog（英文博客）', SITEURL_ROOT + '/blog/en'),
            )
