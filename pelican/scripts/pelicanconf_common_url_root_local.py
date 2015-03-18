#===========================================================================
# RL defined variables
#---------------------------------------------------------------------------

# NOTE: 
# SITEURL_ROOT must set to an absolute domain URL, otherwise the pelican's
# varialbe "SITEURL" will be invalid for DISQUS with error message like: 
#
#   We were unable to load Disqus. If you are a moderator please see our
#   troubleshooting guide.
# 
# If not use DISQUS, it's OK to just set: SITEURL_ROOT = ''

SITEURL_ROOT = 'http://localhost:8000/'      # for debug (don't use an empty string, otherwise disqus won't work - see above comment)

#===========================================================================
