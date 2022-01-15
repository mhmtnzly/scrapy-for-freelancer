from pydoc import describe
import scrapy
import time

class freeSpider(scrapy.Spider):
    name = 'freelance'
    
    start_urls = ['https://www.pewtrusts.org/en/research-and-analysis/data-visualizations/2019/state-broadband-policy-explorer']

    def parse(self, response):
        for item in response.xpath("//div[@class='js-list-item src-views-results-list-view--listItem']"):
            title=item.xpath("//div[@class='src-views-results-list-view--itemHeader flex space-between']/p/text()").getall()
            h2=item.css('h2.src-views-results-list-view--itemHed::text').get()
            description=item.css('p.src-views-results-list-view--itemTitle::text').get()
            category=item.css('p.src-views-results-list-view--category::text').get()
            topic=item.css('p.src-views-results-list-view--topic::text').get()
            full=item.xpath('p[last()]/text()').get()
            yield {
                'place': title[0],
                'year' : title[1],
                'title': h2,
                'description':description,
                'category':category,
                'topic':topic,
                'full':full }