import scrapy
from datetime import datetime
import sys
sys.path.append('./util')
import file_handler

def scrapeCompanyPrice(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::text').get()

def scrapeCompanySymbol(response):
      quote_header_info = response.css('div[id="quote-header-info"]')
      return quote_header_info.css('fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()

class YahooSpider(scrapy.Spider):
    name = "yahoo"
    def start_requests(self):
        file_handler.create_stock_info_file('Yahoo')
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
           yahoo_url = single_stock_urls['yahoo']
           yield scrapy.Request(url=yahoo_url, callback=self.parse)

    def parse(self, response):
      company_name = response.css('h1::text').get()
      symbol = scrapeCompanySymbol(response)
      price = scrapeCompanyPrice(response)
      stock_info = { 'company_name': company_name, 'price': price }
      file_handler.write_stock_info(symbol, stock_info, 'Yahoo')