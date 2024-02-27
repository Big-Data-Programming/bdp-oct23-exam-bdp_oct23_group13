# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    job_role=scrapy.Field()
    website = scrapy.Field()
    reputation = scrapy.Field()
    reached = scrapy.Field()
    questions=scrapy.Field()
    answers=scrapy.Field()
    profiles=scrapy.Field()
    Tags=scrapy.Field()
    
    
    pass
