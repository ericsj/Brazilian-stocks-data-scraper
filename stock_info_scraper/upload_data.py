import requests
import json
import logging

def upload_data(source):
    API_URL = f'http://localhost:5000/stock-data'
    try:
        with open(f'stock_info_scraper/data/{source}.json', 'r') as read_file:
            content = json.load(read_file)
            if content['data']:
                all_stocks_data = content['data']
                headers = {'content-type': 'application/json'}
                for stock_data in all_stocks_data.items():
                    stock_data[1]['acronym'] = stock_data[0]
                    try:
                        if stock_data[1]['name'] or stock_data[1]['price'] or\
                            stock_data[1]['sector'] or stock_data[1]['priceProfitRatio'] or\
                                stock_data[1]['netWorth']:
                                    stock_data[1]['source'] = source
                                    requests.post(API_URL, data=json.dumps(
                                        stock_data[1], indent=4), headers=headers)
                    except Exception:
                        logging.exception('')

    except Exception:
        print(f'{source} data not uploaded')
        logging.exception('')

def main():
    print('uploading...')
    upload_data('Yahoo')
    upload_data('Fundamentus')


if __name__ == '__main__':
    main()
