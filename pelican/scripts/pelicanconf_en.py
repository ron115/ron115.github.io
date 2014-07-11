#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.getcwd()+'/scripts')
from pelicanconf_common import *

AUTHOR = 'Ron'
SITENAME = "My Site"
SITEURL = SITEURL_ROOT + '/article/en'
DEFAULT_LANG = 'en'
MENUITEMS = (
            ('Chinese (中文)', SITEURL_ROOT + '/article/zh'),
            )
DISPLAY_PAGES_ON_MENU = True
