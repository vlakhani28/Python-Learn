import scrapy
from openpyxl import Workbook
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       fp = Workbook()
       sheet = fp.active
       i = 0
       j = 1
       while i!=None :
        quote = response.css("div.quote")[i]
        j = j+1
        s = str(j)
        text = quote.css("span.text::text").get()
        author = quote.css("small.author::text").get()
        sheet["A"+s] = text
        sheet["B"+s] = author
        fp.save(filename = "data.xlsx")
        i = i+1