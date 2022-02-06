import json
import csv
from os import read

def write_json(file_name, data):
    with open(file_name, 'w') as write_file:
      write_file.write(json.dumps(data, indent=4))

def read_json(file_name):
    with open(file_name, 'r') as read_file:
      data = json.load(read_file)
    return data

def write_stock_info(stock_acronym, stock_info, source, time):
  with open(f'data/{source}/{time}.csv', mode='a') as append_file:
    file_writter = csv.writer(append_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writter.writerow([stock_acronym, stock_info])
