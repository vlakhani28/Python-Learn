# -*- coding: utf-8 -*-

import os
import zlib
import redis
try:
    import cPickle
except:
    pass
from hashlib import md5
from news_crawl import settings


class BaseCrawler(object):
    """
    this is base crawler class for news crawlers
    """

    def __init__(self):
        self.redis = redis.Redis()
        self.crawl_data = os.path.join(settings.BASE_DIR, "crawl_data/")
        self.count = 0
        self.failed = 0

    def get_crawl_data_path(self, source):
        """
        this method returns crawl data path for given source
        """
        return os.path.join(self.crawl_data, source)

    def write_to_redis(self, source, path):
        """
        this medhod writes crawl source and its parsed data path refrence to redis cache
        """
        self.redis.rpush(source, path)

    def get_file_name(self, url):
        """
        this method returns md5 hash for crawled url
        which is used as file name
        """
        return md5(url).hexdigest()

    def save_data(self, response, data):
        """
        this method is used to save html response and parsed response to disk
        """
        url = response.url
        html = response.body
        if data.get("daily"):
            source = "daily"
        else:
            source = data["source"]
        base_path = self.get_crawl_data_path(source)
        filename = self.get_file_name(url)

        dir_path = os.path.join(base_path, filename[:2], filename[2:4])
        html_file_path = os.path.join(dir_path, filename + ".html")
        data_file_path = os.path.join(dir_path, filename + ".dat")

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # with open(html_file_path, "wb") as html_file:
        #     html_file.write(html)

        with open(data_file_path, "wb") as out:
            out.write(zlib.compress(cPickle.dumps(data)))

        self.write_to_redis(source, data_file_path)
        print(data_file_path)
