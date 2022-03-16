from symtable import Symbol
import file_handler
from contextlib import nullcontext
import scrapy
from datetime import datetime
import sys
sys.path.append('./util')


def scrape_company_acronym(response):
    quote_header_info = response.css('div[id="quote-header-info"]')
    acronym = quote_header_info.css(
        'fin-streamer[data-field="regularMarketPrice"]::attr(data-symbol)').get()
    return acronym


def scrape_company_net_worth(response):
    # all_statistics_div = response.css('section[data-test="qsp-statistics"]').xpath('div')
    # if len(all_statistics_div) > 1:
    #   all_statistics_div = response.css('section[data-test="qsp-statistics"]').xpath('div')[1]
    #   finances_highlights = all_statistics_div.xpath('div')[2]
    #   finances_highlights_div = finances_highlights.xpath('div')
    #   balance = finances_highlights_div.xpath('div')[4]
    #   balance_tbody = balance.xpath('//tbody')
    #   debt_row = balance_tbody.xpath('tr')[4]
    #   debt = debt_row.xpath('td')[1].extract()
    #   return debt
    #   debt_divided_by_net_worth = response.css('td[data-test="PE_RATIO-value"]::text').get()
    #   if debt_divided_by_net_worth:
    #     return debt / debt_divided_by_net_worth
    return None


class YahooSpider(scrapy.Spider):
    name = "yahoo-statistics"

    def start_requests(self):
        urls = file_handler.read_json('data/links.json')
        for single_stock_urls in urls.values():
            yahoo_url = single_stock_urls['yahoo_statistics']
            yield scrapy.Request(url=yahoo_url, callback=self.parse)

    def parse(self, response):
        file_handler.append_stock_info(scrape_company_acronym(response),
                                       'netWorth', scrape_company_net_worth(response), 'Yahoo')
