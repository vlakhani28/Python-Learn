import scrapy
from openpyxl import Workbook
class QuotesSpider(scrapy.Spider):
    name = "solarx"

    def start_requests(self):
        urls = ["https://dir.indiamart.com/impcat/solar-panels.html"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       fp = Workbook()
       sheet = fp.active
       i = 0
       j = 1
       #while i!=None :
       p = response.xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/ul/li[1]/div/div[1]")[0].extract()
       #image = p.xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/ul/li[1]/div/div[1]/div[1]/img]").extract()    
       #print(image)
       j = j+1
       s = str(j)
       title = p.xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/ul/li[1]/div/div[1]/div[2]/a[1]/h3/text()").extract()
       print(title)        
       price = p.xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/ul/li[1]/div/div[1]/div[2]/p/span/text()").extract()
       print(price)    
       qty = p.xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/ul/li[1]/div/div[1]/div[2]/p/span/span[2]/text()").extract()
       print(qty)
       i = i+1

       """
        sheet["A"+s] = img
        sheet["B"+s] = title
        sheet["C"+s] = price
        sheet["D"+s]= qty
        fp.save(filename = "data1.xlsx")
        """
        