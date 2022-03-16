import scrapy
from datetime import datetime
import sys
sys.path.append('./util')
import file_handler

def scrape_company_symbol(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()[:-3]

def scrape_company_name(response):
      try:
            name = response.css('h1::text').get()
            if name[:2] == ' (':
                  return None
            return name
      except:
            return None

def scrape_company_price(response):
      try:
            quote_header_info = response.css('div[id="quote-header-info"]')
            return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::text').get().replace(',','.')
      except:
            return None

def scrape_company_price_profit_ratio(response):
      try:
            return response.css('td[data-test="PE_RATIO-value"]::text').get().replace(',','.')
      except:
            return None

class YahooSpider(scrapy.Spider):
    name = "Yahoo"
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
        'priceProfitRatio': scrape_company_price_profit_ratio(response),
        'netWorth': None
      }
      file_handler.write_stock_info(scrape_company_symbol(response), stock_info, 'Yahoo')