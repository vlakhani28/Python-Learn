import scrapy
import json
from lxml import etree
from io import StringIO
class QuotesSpider(scrapy.Spider):
    name = "stories1"

    def start_requests(self):
        urls = ["https://www.hawaiibusiness.com"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)        

    def parse(self, response):
        #html = response.body
        #parser = etree.HTMLParser()
        #tree = etree.parse(StringIO(html),parser)
        #https\:\/\/www\.hawaiibusiness\.com\/(([a-z]+|[0-9]+)(-))+([a-z]+|[0-9]+\/)
        #https\:\/\/www\.hawaiibusiness\.com\/.+
        title = response.xpath("//*[@id = 'main']/header/div/div/h1//text()").extract()
        t = response.xpath("//*[@id = 'main']/header/div/div/h5/a//text()").extract()        
        tag = []
        for a in t :
            tag.append(str(a))
        dop = response.xpath("//meta[@property ='article:published_time']/@content").extract()
        img = response.xpath("//*[@id='main']//section[1]//img//@data-src").extract()
        images = []
        for a in img :
            images.append(str(a))
        cover_img = response.xpath("//*[@id='main']//img[@class = 'lazyload']//@data-src").extract()
       
        video = response.xpath("//*[@id='main']//iframe//@src").extract()
        vid = []
        for a in video :
            vid.append(str(a))
        author = response.xpath("//*[@id = 'main']/div[3]/div/aside/div/ul/li/figure/div/h5//text()").extract()
        actual = response.xpath("//*[@id='main']/div[3]/div/section/div[1]/*[not(name()='figure')]//text()").extract()
        text = ""
        for a in actual :
            text = text+a                
  

        data = {}
        data["title"]=title
        data["category"]=tag
        data["Publishing Date"]=dop
        data["Author"]=author
        data["Cover Image"]=cover_img
        data["Other images"]=images
        data["Video"]=vid 
        data["Content"]=text
        with open("data5.json", 'w') as f:
         json.dump(data, f)
