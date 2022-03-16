import scrapy
import sys
sys.path.append('./util')
import file_handler

class LinksSpider(scrapy.Spider):
    name = "links"
    def start_requests(self):
        urls = ['https://www.fundamentus.com.br/detalhes.php?papel=']
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
      acronyms = response.css('tbody tr td a::text').getall()
      fundamentus_links = response.css('tbody tr td a::attr(href)').getall()
      content = {}
      for index in range(len(acronyms)):
        acronyms[index] = acronyms[index].strip()
        content[acronyms[index]] = {
          'fundamentus': f'https://www.fundamentus.com.br/{fundamentus_links[index]}',
          'yahoo': f'https://br.financas.yahoo.com/quote/{acronyms[index]}.SA',
          'yahoo_statistics': f'https://br.financas.yahoo.com/quote/{acronyms[index]}.SA/key-statistics',
          'yahoo_profile': f'https://br.financas.yahoo.com/quote/{acronyms[index]}.SA/profile'
        }
      file_handler.write_json('data/links.json', content)