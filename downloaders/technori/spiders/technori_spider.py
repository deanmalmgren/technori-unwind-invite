from pprint import pprint
import sys
import re

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

from technori.items import TechnoriItem

class TechnoriSpider(BaseSpider):
    name = 'technori_spider'
    allowed_domains = [
        'technori.com'
    ]
    page_url_template = 'http://technori.com/page/%s/'
    start_urls = [
        page_url_template % (1, )
    ]
    page_url_re = re.compile(page_url_template % r'(?P<page>\d+)')

    # handle 404 requests in the parse method
    # http://stackoverflow.com/a/9698718/564709
    handle_httpstatus_list = [404]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # determine the current page number
        try:
            current_url = response.meta["redirect_urls"][0]
        except KeyError:
            current_url = response.url
        current_page = int(self.page_url_re.search(current_url).group('page'))
        
        # this is when we're done
        if response.status == 404:
            self.log("completed pagination at page %s" % current_page)
            yield None

        # parse out all of the article links on the page
        for url in hxs.select('//a[@class="read_more_link"]/@href').extract():
            request = Request(url, callback=self.parse_article)
            yield request
        
        # get the next page of results. the redirect url happens for
        # the first page but everything after that works just fine
        next_page = current_page + 1
        yield Request(self.page_url_template % next_page, callback=self.parse)

    def parse_article(self, response):
        hxs = HtmlXPathSelector(response)
        i = TechnoriItem()
        result = hxs.select("//article/descendant::*[not(ancestor::header) and not(ancestor::footer) and not(ancestor::section)]/text()")
        i["text"] = ' '.join(result.extract())

        return i
        
