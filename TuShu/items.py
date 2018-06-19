# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TushuItem(scrapy.Item):
    # define the fields for your item here like:
    photo = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    xunlei_url = scrapy.Field()
    image_path = scrapy.Field()


# class oneItem(scrapy.Item):
#     # define the fields for your item here like:
#     photo = scrapy.Field()
#     name = scrapy.Field()
#     url = scrapy.Field()
