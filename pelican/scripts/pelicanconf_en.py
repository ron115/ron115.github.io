#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = 'Ron'
SITENAME = "My Site"
SITEURL = SITEURL_EN
DEFAULT_LANG = 'en'
MENUITEMS = (
            ('中文 (Chinese)', SITEURL_ZH),
            )
