import json
from os import read

def write_json(file_name, data):
    with open(file_name, 'w') as write_file:
      write_file.write(json.dumps(data, indent=4))

def read_json(file_name):
    with open(file_name, 'r') as read_file:
      data = json.load(read_file)
    return data

def create_stock_info_file(source):
  file_name = f'data/{source}.json'
  write_json(file_name, {})

def write_stock_info(stock_acronym, stock_info, source):
  file_name = f'data/{source}.json'
  file_content = read_json(file_name)
  file_content[stock_acronym] = stock_info
  write_json(file_name, file_content)

def append_stock_info(stock_acronym, stock_info_key, stock_info_value, source):
  file_name = f'data/{source}.json'
  stock_info = read_json(file_name)
  if stock_acronym in stock_info:
    stock_info[stock_acronym][stock_info_key] = stock_info_value
  write_json(file_name, stock_info)