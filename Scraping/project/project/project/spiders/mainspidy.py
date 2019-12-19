from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import json
from lxml import etree
from io import StringIO
class QuotesSpider(CrawlSpider):
    name = "story"
    allowed_domains = ["hawaiibusiness.com"]
    start_urls = ["https://www.hawaiibusiness.com/"]
    #rules = (Rule(LinkExtractor(allow=["https\:\/\/www\.hawaiibusiness\.com\/(([a-z]+|[0-9]+)(-))+([a-z]+|[0-9]+\/)"]),callback = 'parse',follow = True,),)
    rules = (Rule(LinkExtractor(allow=["https\:\/\/www\.hawaiibusiness\.com\/.+"]),callback = 'parse_item',follow = True,),)


    def parse_item(self, response):
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
  
        filename = str(title)+".json"
        data = {}
        data["title"]=title
        data["category"]=tag
        data["Publishing Date"]=dop
        data["Author"]=author
        data["Cover Image"]=cover_img
        data["Other images"]=images
        data["Video"]=vid 
        data["Content"]=text
        with open(filename, 'w') as f:
            json.dump(data, f)