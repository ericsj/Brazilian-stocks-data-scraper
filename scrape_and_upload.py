import os
import sys
sys.path.append('./stock_info_scraper')
import upload_data

os.system('cd stock_info_scraper;\
    scrapy crawl links;\
    scrapy crawl Yahoo;\
    scrapy crawl Yahoo-profile;\
    scrapy crawl Fundamentus;')

upload_data.main()