import file_handler
from contextlib import nullcontext
import scrapy
from datetime import datetime
import sys
sys.path.append('./util')


def scrape_company_acronym(response):
    quote_header_info = response.css('div[id="quote-header-info"]')
    return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()


def scrape_company_sector(response):
    try:
        return response.xpath(
            '//div[@class="asset-profile-container"]/div/div/p')[1].xpath('span/text()')[1].get()
    except:
        return ''


class YahooSpider(scrapy.Spider):
    name = "yahoo-profile"

    def start_requests(self):
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
            yahoo_url = single_stock_urls['yahoo_profile']
            yield scrapy.Request(url=yahoo_url, callback=self.parse)

    def parse(self, response):
        file_handler.append_stock_info(scrape_company_acronym(response),
                                       'sector', scrape_company_sector(response), 'Yahoo')
