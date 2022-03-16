import scrapy
from datetime import datetime
import sys
sys.path.append('./util')
import file_handler

def scrape_company_symbol(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()

def scrape_company_name(response):
      return response.css('h1::text').get()

def scrape_company_price(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::text').get()

def scrape_company_price_profit_ratio(response):
      return response.css('td[data-test="PE_RATIO-value"]::text').get()

class YahooSpider(scrapy.Spider):
    name = "yahoo"
    def start_requests(self):
        file_handler.create_stock_info_file('Yahoo')
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
           yahoo_url = single_stock_urls['yahoo']
           yield scrapy.Request(url=yahoo_url, callback=self.parse)

    def parse(self, response):
      stock_info = {
        'name': scrape_company_name(response),
        'price': scrape_company_price(response),
        'priceProfitRatio': scrape_company_price_profit_ratio(response)
      }
      file_handler.write_stock_info(scrape_company_symbol(response), stock_info, 'Yahoo')