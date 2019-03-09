# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    rent_way = scrapy.Field()
    rent_type = scrapy.Field()
    rent_area = scrapy.Field()
    rent_dire = scrapy.Field()
    floor = scrapy.Field()
    elevator = scrapy.Field()