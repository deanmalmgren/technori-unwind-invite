# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import re
import unicodedata
import nltk

class ReplaceSpecialCharacters(object):
    def process_item(self, item, spider):
        # item["text"] = item["text"].replace(u'\xa0', ' ')
        # # item["text"] = item["text"].encode('ascii', errors="ignore")
        item["text"] = unicodedata.normalize('NFKD', item["text"])\
            .encode('ascii','ignore')
        return item

class RemoveWhitespace(object):
    whitespace_re = re.compile(r"\s\s+")
    def process_item(self, item, spider):
        item["text"] = self.whitespace_re.sub(' ', item["text"])
        return item

class RemovePunctuation(object):
    punctuation_re = re.compile(r"[^\w\s]")
    def process_item(self, item, spider):
        item["text"] = self.punctuation_re.sub('', item["text"])
        return item

class LowerCase(object):
    def process_item(self, item, spider):
        item["text"] = item["text"].lower()
        return item

class RemoveNumbers(object):
    """reduce the number of words that are stored"""
    numbers_re = re.compile(r"\s\d+\s")
    def process_item(self, item, spider):
        item["text"] = self.numbers_re.sub(' ', item["text"])
        return item

class RemoveStopwords(object):
    """remove stopwords from the analysis"""
    stopwords = set(nltk.corpus.stopwords.words('english'))
    def process_item(self, item, spider):
        print self.stopwords
        item["text"] = ' '.join(
            w for w in item["text"].split() if w not in self.stopwords
        )
        return item
