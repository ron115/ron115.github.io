#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = '李某'
SITENAME = "Pelican Test"
SITEURL = SITEURL_ZH
DEFAULT_LANG = 'zh_cn'
MENUITEMS = (
            ('English (英文)', SITEURL_EN),
            )
