# Scrapy settings for technori project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'technori'

SPIDER_MODULES = [
    'technori.spiders'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'technori (+http://www.yourdomain.com)'

# use a local cache instead of hitting the webpage during debugging
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0 # Set to 0 to never expire
