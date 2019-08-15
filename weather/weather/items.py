# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherPerHourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # time in  the day
    time = scrapy.Field()

    # what's the weather this day
    weather = scrapy.Field()

    # what's the temperature
    temperature = scrapy.Field()
