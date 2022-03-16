import requests
import json


def upload_data(source):
    API_URL = f'http://localhost:5000/stock-data'
    with open(f'data/{source}.json', 'r') as read_file:
        content = json.load(read_file)
        if content['data']:
            all_stocks_data = content['data']
            headers = {'content-type': 'application/json'}
            for stock_data in all_stocks_data.items():
                stock_data[1]['acronym'] = stock_data[0]
                stock_data[1]['source'] = source
                # requests.put(API_URL, data=json.dumps(
                #     stock_data[1], indent=4), headers=headers)


def main():
    upload_data('Yahoo')
    upload_data('Fundamentus')


if __name__ == '__main__':
    main()
