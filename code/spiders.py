import scrapy
import pandas as pd
from ..items import SpiderItem
import time

class SpidersSpider(scrapy.Spider):
    name = "spiders"
    
    df = pd.read_excel('/Users/rakeshnagaragattajayanna/Downloads/stackoverflow_50k_records.xlsx')  # Update the path as needed
    # start_urls = df['link'].iloc[334:].tolist()
    start_urls = df['link'].iloc[0:].dropna().astype(str).tolist()


    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'output.csv',
        'AUTOTHROTTLE_START_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.3'
    }

    def parse(self, response):
        time.sleep(2)
        items = SpiderItem()
        # items['name']= response.css('.flex--item.mb12.fs-headline2.lh-xs::text').extract()
        # items['job_role']= response.css('.mb8.fc-black-400.fs-title.lh-xs::text').extract()
        # items['website']= response.css('.flex--item a.flex--item::text').extract()
        # items['Tags']=response.css('.flex--item.ws-nowrap a.s-tag.js-hoverable-post-tag.js-gps-track::text').extract()
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
            'profiles': [],
            'reputation': '',
            'reached': '',
            'questions': '',
            'answers': ''
        }
        

        extracted_data = response.css('.flex--item.ml-auto .d-flex.gsx.gs16 .fs-body3.mr4::text').extract()

        if extracted_data:
            items['reputation'] = extracted_data[0].strip() if len(extracted_data) > 0 else ''
            items['reached'] = extracted_data[1].strip() if len(extracted_data) > 1 else ''
            items['questions'] = extracted_data[2].strip() if len(extracted_data) > 2 else ''
            items['answers'] = extracted_data[3].strip() if len(extracted_data) > 3 else ''

           
            for i in range(4, len(extracted_data), 3):
                if i + 2 < len(extracted_data):
                    profile = {
                        'score': extracted_data[i].strip(),
                        'post': extracted_data[i + 1].strip(),
                        'posts': extracted_data[i + 2].strip()
                    }
                    items['profiles'].append(profile)

        yield items
