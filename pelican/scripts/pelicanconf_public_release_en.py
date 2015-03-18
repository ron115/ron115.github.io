#===========================================================================
# for "import xxx" so that update_xxx.bat files can work
#---------------------------------------------------------------------------

import os
import sys
sys.path.append(os.getcwd()+'/scripts')

#===========================================================================

from pelicanconf_common_en import *
from pelicanconf_common_url_root_public import *

SITEURL = SITEURL_ROOT + OUTPUT_DIR_NAME
