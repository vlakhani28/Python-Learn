from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from parsers.manufacturingindiatoday_parser import parse_data
from base_crawler import BaseCrawler


class ManufacturingTodayIndia(CrawlSpider, BaseCrawler):
    name = "mitoday"
    allowed_domains = ["manufacturingtodayindia.com"]
    start_urls = ["https://www.manufacturingtodayindia.com/",
                  "https://www.manufacturingtodayindia.com/sectors",
                  "https://www.manufacturingtodayindia.com/people",
                  "https://www.manufacturingtodayindia.com/products-suppliers",
                  "https://www.manufacturingtodayindia.com/events",
                   ]
    rules = (
        Rule(LinkExtractor(allow=['https\:\/\/www\.manufacturingtodayindia\.com\/(sectors|products-suppliers|people|events|\d\d\d\d|\w.+).+'
                                    ,'((?!\?page=(\d\d\d|\d\d|\d)).)*']), callback='parse_page', follow=True,),
    )

    def __init__(self):
        CrawlSpider.__init__(self)
        BaseCrawler.__init__(self)


    def parse_page(self, response):
        super(ManufacturingTodayIndia, self).parse(response)
        try:
            data = parse_data(response)
            self.save_data(response, data)
            self.count += 1
        except Exception as e:
            msg = "Failed: {0} Exception:{1}".format(response.url, e)
            self.logger.error(msg)
            self.failed += 1
            print(data)
        print("Total Count: {0}".format(self.count))
        print("Total Failed: {0}".format(self.failed))
