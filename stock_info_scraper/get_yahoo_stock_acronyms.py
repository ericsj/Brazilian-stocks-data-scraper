import requests
import sys
sys.path.append('util')
import file_handler

def test_acronym_not_sufixed(acronym):
    headers = {
        'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }
    url = "https://br.financas.yahoo.com/quote/" + acronym + '.SA'
    r = requests.get(url, headers=headers)
    print(r.url, r.status_code)
    return r.status_code in range(200, 299)

def transform_acronym(acronym, needs_sa_sufix):
    new_acronym = acronym
    if needs_sa_sufix:
        new_acronym += '.SA'
    return new_acronym

def get_yahoo_acronyms(stock_acronym_list):
    new_acronym_list = []
    for acronym in stock_acronym_list:
        needs_sa_sufix = not test_acronym_not_sufixed(acronym)
        new_acronym_list.append(transform_acronym(acronym, needs_sa_sufix))
    return new_acronym_list

def main():
    yahoo_stocks_names_and_acronyms = {}
    stocks_names_and_acronyms = file_handler.read_json('data/Infomoney/stocks-names-and-acronyms.json')
    for name in stocks_names_and_acronyms:
        yahoo_stocks_names_and_acronyms[name] = get_yahoo_acronyms(stocks_names_and_acronyms[name])
    file_handler.write_json('data/Yahoo/stocks-names-and-acronyms.json', yahoo_stocks_names_and_acronyms)

if __name__ == "__main__":
    main()