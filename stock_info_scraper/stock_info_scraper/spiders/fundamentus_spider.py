import scrapy
from datetime import datetime
import sys
sys.path.append('./util')
import file_handler

def scrape_company_symbol(response):
  return response.xpath('//tr')[0].xpath('td')[1].css('span::text').get()

def scrape_company_name(response):
  return response.xpath('//tr')[2].xpath('td')[1].css('span::text').get()

def scrape_company_price(response):
  return response.xpath('//tr')[0].xpath('td')[3].css('span::text').get()

def scrape_company_price_profit_ratio(response):
  return response.xpath('//table')[2].xpath('tr')[1].xpath('td')[3].xpath('span/text()')[0].extract()

class FundamentusSpider(scrapy.Spider):
    name = "fundamentus"
    def start_requests(self):
        file_handler.create_stock_info_file('Fundamentus')
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
           url = single_stock_urls['fundamentus']
           yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
      stock_info = {
        'company_name': scrape_company_name(response),
        'price': scrape_company_price(response),
        'price_profit_ratio': scrape_company_price_profit_ratio(response)
      }
      file_handler.write_stock_info(scrape_company_symbol(response), stock_info, 'Fundamentus')