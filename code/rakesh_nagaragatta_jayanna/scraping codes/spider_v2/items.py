# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    People_reached = scrapy.Field()
    Posts_edited=scrapy.Field()
    helpful_tags = scrapy.Field()
    votes_cast = scrapy.Field()
    Upvotes= scrapy.Field()
    downvotes=scrapy.Field()
    question_vote= scrapy.Field()
    answer_votes=scrapy.Field()
    this_month= scrapy.Field()
    Name = scrapy.Field()
    Location= scrapy.Field() 
    
    
  
    
    
    pass
