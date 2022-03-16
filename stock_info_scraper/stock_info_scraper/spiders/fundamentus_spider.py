import sys
from datetime import datetime
import scrapy
sys.path.append('./util')
import file_handler


def scrape_company_symbol(response):
    return response.xpath('//tr')[0].xpath('td')[1].css('span::text').get().strip()

def scrape_company_name(response):
    try:
        return response.xpath('//tr')[2].xpath('td')[1].css('span::text').get()
    except:
        return None


def scrape_company_price(response):
    try:
        return response.xpath('//tr')[0].xpath('td')[3].css('span::text').get().replace(',', '.')
    except:
        return None


def scrape_company_sector(response):
    try:
        return response.xpath('//tr')[3].xpath('td')[1].css('span a::text').get()
    except:
        return None


def scrape_company_price_profit_ratio(response):
    try:
        return response.xpath('//table')[2].xpath('tr')[1].xpath('td')[3].xpath('span/text()')[0].extract().replace(',', '.')
    except:
        return None


def scrape_company_net_worth(response):
    try:
        return response.xpath('//table')[3].xpath('tr')[3].xpath('td')[3].xpath('span/text()').get().replace('.','')
    except:
        return None


class FundamentusSpider(scrapy.Spider):
    name = "Fundamentus"

    def start_requests(self):
        file_handler.create_stock_info_file('Fundamentus')
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
            url = single_stock_urls['fundamentus']
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        stock_info = {
            'name': scrape_company_name(response),
            'price': scrape_company_price(response),
            'sector': scrape_company_sector(response),
            'priceProfitRatio': scrape_company_price_profit_ratio(response),
            'netWorth': scrape_company_net_worth(response),
        }
        file_handler.write_stock_info(scrape_company_symbol(
            response), stock_info, 'Fundamentus')
