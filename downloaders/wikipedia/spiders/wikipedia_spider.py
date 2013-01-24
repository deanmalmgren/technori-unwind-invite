from pprint import pprint
import sys
import re

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

from wikipedia.items import WikipediaItem

class WikipediaSpider(BaseSpider):
    name = 'wikipedia_spider'
    allowed_domains = [
        'en.wikipedia.com',
    ]
    start_urls = [
        'http://en.wikipedia.org/wiki/Entrepreneurship',
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        content_hxs = hxs.select('//div[@id="mw-content-text"]')[0]
        print content_hxs

        print 'helllllo'

        # get the text of the item
        i = WikipediaItem()
        i["text"] = content_hxs

        # # parse out all of the article links on the page
        # for url in hxs.select('//a[@class="read_more_link"]/@href').extract():
        #     request = Request(url, callback=self.parse_article)
        #     yield request



        
        # # get the next page of results. the redirect url happens for
        # # the first page but everything after that works just fine
        # next_page = current_page + 1
        # yield Request(self.page_url_template % next_page, callback=self.parse)

    # def parse_article(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     i = WikipediaItem()
    #     result = hxs.select("//article/descendant::*[not(ancestor::header) and not(ancestor::footer) and not(ancestor::section)]/text()")
    #     i["text"] = ' '.join(result.extract())

    #     return i
        
