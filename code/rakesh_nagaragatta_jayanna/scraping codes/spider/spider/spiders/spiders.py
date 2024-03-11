import scrapy
import pandas as pd
from ..items import SpiderItem
import time

class SpidersSpider(scrapy.Spider):
    name = "spiders"
    
    df = pd.read_excel('/Users/rakeshnagaragattajayanna/Downloads/stackoverflow_50k_records.xlsx')
    start_urls_info = list(zip(df['user_id'].dropna(), df['link'].dropna().astype(str)))


    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'output.csv',
        'AUTOTHROTTLE_START_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.3'
    }
    def start_requests(self):
        for user_id, link in self.start_urls_info:
            yield scrapy.Request(url=link, callback=self.parse, meta={'user_id': user_id})


    def parse(self, response):
        time.sleep(2)
        items = SpiderItem()
        items['user_id'] = response.meta['user_id']

        badges = response.css('div.d-flex.flex__fl-equal.fw-wrap.gs24 .flex--item.s-card.bar-md .fs-title.fw-bold.fc-black-600::text').extract()
        gold_badges = '0'
        silver_badges = '0'
        bronze_badges = '0'
        if len(badges) >= 1:
            gold_badges = badges[0].strip()
        if len(badges) >= 2:
            silver_badges = badges[1].strip()
        if len(badges) == 3:
            bronze_badges = badges[2].strip()
        items = {
            'name': response.css('.flex--item.mb12.fs-headline2.lh-xs::text').extract(),
            'job_role': response.css('.mb8.fc-black-400.fs-title.lh-xs::text').extract(),
            'website': response.css('.flex--item a.flex--item::text').extract(),
            'Tags':response.css('.flex--item.ws-nowrap a.s-tag.js-hoverable-post-tag.js-gps-track::text').extract(),
            'Member_Since':response.css('ul.list-reset.s-anchors.s-anchors__inherit.d-flex.fc-black-400.gs8.mln4.fw-wrap .d-flex.gs4.gsx.ai-center .flex--item span::text').extract(),
            'gold_badges': gold_badges,
            'silver_badges': silver_badges,
            'bronze_badges': bronze_badges,
            'reputation': '',
            'reached': '',
            'questions': '',
            'answers': ''
        }
        

        extracted_data = response.css('.fs-body3.fc-black-600::text').extract()
        items['user_id'] = response.meta['user_id'] 
        if extracted_data:
            items['reputation'] = extracted_data[0].strip() if len(extracted_data) > 0 else ''
            items['reached'] = extracted_data[1].strip() if len(extracted_data) > 1 else ''
            items['answers'] = extracted_data[2].strip() if len(extracted_data) > 2 else ''
            items['questions'] = extracted_data[3].strip() if len(extracted_data) > 3 else ''

        yield items
