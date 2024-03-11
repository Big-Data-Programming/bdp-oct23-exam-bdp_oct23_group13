import scrapy
import pandas as pd
from ..items import SpiderItem
import time

class SpidersSpider(scrapy.Spider):
    name = "spiders"
    
    df = pd.csv('/Users/rakeshnagaragattajayanna/Downloads/profiles_links.csv')  # Update the path as needed
    start_urls = df['link'].iloc[0:].dropna().astype(str).tolist()

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'FEED_FORMAT': 'csv',
        # 'FEED_URI': 'output.csv',
        'AUTOTHROTTLE_START_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.3'
    }

    def parse(self, response):
    
        items = SpiderItem()

    
        extracted_data = response.css('.flex--item .fs-body3.fc-black-600::text').extract()
        cleaned_data = [data.strip() for data in extracted_data if data.strip()]

    
        label_names = ['People_reached', 'Posts_edited', 'helpful_tags', 'votes_cast']
        
   
        for i, label in enumerate(label_names):
            items[label] = cleaned_data[i] if i < len(cleaned_data) else '0'
        
 
        location = response.css('.wmx2.truncate::text').extract_first(default='Not Available')
        items['Location'] = location.strip() if location else 'Not Available'

 
        name = response.css('.flex--item.mb12.fs-headline2.lh-xs::text').extract_first(default='Not Available')
        items['Name'] = name.strip() if name else 'Not Available'


        yield items
