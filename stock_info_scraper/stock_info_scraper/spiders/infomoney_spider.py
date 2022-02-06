import scrapy
import json
 
def scrape_stock_name(response, data):
   stock_price_name = response.css('h1::text').get()
   data['name'] = stock_price_name
 
def scrape_stock_price(response, data):
   stock_price_div = response.css('div.value')
   stock_price_value = stock_price_div.css('p::text').get()
   data['price'] = stock_price_value
 
def scrape_stock_sector(response, data):
   stock_about_div = response.css('div.about')
   stock_about_h3s = stock_about_div.css('h3')
   data['sector'] = stock_about_h3s[2].css('strong::text').get()
 
def write_data(data):
   with open('infomoney.json', 'w') as outfile:
       json.dump(data, outfile)
 
class Infomoney(scrapy.Spider):
   name = 'infomoney'
  
   def start_requests(self):
       urls = ["https://www.infomoney.com.br/cotacoes/petrobras-petr4/"]
       for url in urls:
           yield scrapy.Request(url=url, callback=self.parse)

   def parse(self, response):
       data = {}
       scrape_stock_name(response, data)
       scrape_stock_price(response, data)
       scrape_stock_sector(response, data)
       write_data(data)
