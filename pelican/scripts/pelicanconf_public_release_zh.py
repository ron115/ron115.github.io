#===========================================================================
# for "import xxx" so that update_xxx.bat files can work
#---------------------------------------------------------------------------

import os
import sys
sys.path.append(os.getcwd()+'/scripts')

#===========================================================================

from pelicanconf_common_zh import *
from pelicanconf_common_public_url_root import *

SITEURL = SITEURL_ROOT + OUTPUT_DIR_NAME
