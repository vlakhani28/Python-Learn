import scrapy
from openpyxl import Workbook
class QuotesSpider(scrapy.Spider):
    name = "solar"

    def start_requests(self):
        urls = ["https://dir.indiamart.com/impcat/solar-panels.html"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       fp = Workbook()
       sheet = fp.active
       i = 0
       j = 1
       while i!=None :
        p = response.css("div.l-cl.b-w")[i]
        image = p.css("div.prd-img").get().strip()
        img = str(image)        
        j = j+1
        s = str(j)
        title = p.css("h3.lg::text").get()
        price = p.css("span.prc.cur::text").get()
        qty = p.css("span.quan::text").get()
        sheet["A"+s] = img
        sheet["B"+s] = title
        sheet["C"+s] = price
        sheet["D"+s]= qty
        fp.save(filename = "data.xlsx")
        i = i+1