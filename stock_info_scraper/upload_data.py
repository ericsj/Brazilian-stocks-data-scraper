import requests
import json

def upload_data(source):
  API_URL = f'http://localhost:5000/{source}'
  with open(f'data/{source}.json', 'r') as read_file:
    content = json.load(read_file)
    headers = { 'content-type': 'application/json' }
    print(type(content))
    requests.put(API_URL, data=json.dumps(content, indent=4), headers=headers)

def main():
  upload_data('Yahoo')

if __name__ == '__main__':
  main()