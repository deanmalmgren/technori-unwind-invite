# Scrapy settings for technori project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'technori'

SPIDER_MODULES = [
    'technori.spiders',
    'wikipedia.spiders',
]
NEWSPIDER_MODULE = 'technori.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'technori (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    'technori.pipelines.ReplaceSpecialCharacters',
    'technori.pipelines.RemoveWhitespace',
    'technori.pipelines.RemovePunctuation',
    'technori.pipelines.LowerCase',
    'technori.pipelines.RemoveNumbers',
    'technori.pipelines.RemoveStopwords',
]

# wait between 0.5*DOWNLOAD_DELAY ms and 1.5*DOWNLOAD_DELAY ms before
# requesting next page from the same spider
DOWNLOAD_DELAY = 3.0
RANDOMIZE_DOWNLOAD_DELAY = True

# reduce log spew http://stackoverflow.com/questions/14390945
LOG_LEVEL = 'INFO'

# use a local cache instead of hitting the webpage during debugging
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0 # Set to 0 to never expire

