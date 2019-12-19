import re
import json 
import requests

from lxml import etree
from StringIO import StringIO

def parse_data(response):
    html = response.body
    url = response.url
    source = "manufacturingtodayindia.com"

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    title = source_url = cover_image = blurb = full_text = published_on = \
    active = author = author_twitter = total_views = total_comments = category = ""
    actual_images = video_data = breadcrumb = tags = desc_text = []

    category_ele = tree.xpath("//div[@class='custom-sec']/a/text()")
    if category_ele:
        category = category_ele[0].strip()

    author_ele = tree.xpath("//span[@class='author-name']/a/text()")
    if author_ele:
        author = author_ele[0].strip()

    published_on_ele = tree.xpath("//span[@class='time']/text()")
    if published_on_ele:
        published_on = published_on_ele[0].strip()

    title_ele = tree.xpath("//div[@class='tle-wrp']/h1/text()")
    if title_ele:
        title = title_ele[0].strip() 

    images = tree.xpath("//div[@class='img-container dmb ar-sp mb-nmr']//img//@src")
    actual_images = []
    if images:
        for img in images:
            actual_images.append(str(img))
        if actual_images:
            cover_image = actual_images[0]

    more_images = tree.xpath("//div[@class='body-content clearfix']")
    if more_images:
        for child in more_images[0].iterchildren():
            if child.tag == "p":
                for innerchild in child.iterchildren():
                        if innerchild.tag == "img":
                            img = innerchild.xpath(".//@src")
                            actual_images.append(str(img))

    initial_desc = tree.xpath("//div[@class='tle-wrp']/h2/text()")
    full_text = []
    if initial_desc:
        initial_desc = initial_desc[0].encode("utf-8", "ignore").strip()
    else:
        initial_desc = ""

    if initial_desc:
        desc_text.append(initial_desc)

    full_text_ele = tree.xpath("//div[@class='body-content clearfix']")
    if full_text_ele:
        for child in full_text_ele[0].iterchildren():
            if child.tag in ["p","div","li","ol","ul"]:
                if child.tag == "div":
                    for innerchild in child.iterchildren():
                        if innerchild.tag == "p":
                            text_values = innerchild.xpath(".//text()")
                            if text_values:
                                text_values = [i.strip() for i in text_values if i.strip()]
                                text = " ".join(text_values)
                                desc_text.append(text)
                            else:
                                continue
                else:
                    text_values = child.xpath(".//text()")
                    if text_values:
                        text_values = [i.strip() for i in text_values if i.strip()]
                        text = " ".join(text_values)
                        desc_text.append(text)
        full_text = "\n".join([i.replace('\n', ' ').strip().encode('ascii','ignore') for i in desc_text])            

    tags_ele = tree.xpath("//ul[@class='content-tags clearfix']//li//text()")
    if tags_ele:
        try:
            tags = [i.strip() for i in tags_ele if i.strip()]
        except Exception:
            tags = []
    else:
        tags = []        

    result = {}
    result["title"] = str(title.encode('utf-8','ignore'))
    result["source"] = str(source)
    result["source_url"] = str(url)
    result["cover_image"] = str(cover_image)
    result["blurb"] = str(full_text)
    result["full_text"] = str(full_text)
    result["published_on"] = str(published_on.encode('utf-8','ignore'))
    result["active"] = str(active)
    result["author"] = str(author.encode('utf-8','ignore'))
    result["category"] = str(category)
    result["video_data"] = []
    result["images"] = list(actual_images)
    result["breadcrumb"] = list(breadcrumb)
    result["tags"] = list(tags)

    return result            