from contextlib import nullcontext
import scrapy
from datetime import datetime
import sys
sys.path.append('./util')
import file_handler

def scrape_company_symbol(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()

def scrape_company_net_worth(response):
  return None

class YahooSpider(scrapy.Spider):
    name = "yahoo-statistics"
    def start_requests(self):
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
           yahoo_url = single_stock_urls['yahoo_statistics']
           yield scrapy.Request(url=yahoo_url, callback=self.parse)

    def parse(self, response):
      file_handler.append_stock_info(scrape_company_symbol(response),
        'net_worth', scrape_company_net_worth(response), 'Yahoo')