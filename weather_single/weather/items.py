# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherPerHourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    city = scrapy.Field()
    date = scrapy.Field()

    # what's the weather today
    weather = scrapy.Field()

    # what's the temperature
    temperature_high = scrapy.Field()
    temperature_low = scrapy.Field()

    # wind
    wind = scrapy.Field()
