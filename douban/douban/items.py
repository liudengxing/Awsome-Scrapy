# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Ranking number
    number = scrapy.Field()

    # Movie name
    title = scrapy.Field()

    # Star
    rating_num = scrapy.Field()

    # How many people grade
    rating_person = scrapy.Field()

    # The introduce of the movie
    introduce = scrapy.Field()

    # Ten word to describe the movie
    describe = scrapy.Field()
