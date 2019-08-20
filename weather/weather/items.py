# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # which city
    city = scrapy.Field()

    # weather form morning to the evening
    weather_morning = scrapy.Field()
    weather_evening = scrapy.Field()

    # Maybe the wind is strong
    wind_morning = scrapy.Field()
    wind_evening = scrapy.Field()

    # i hava to say it's too hot in fuzhou
    temperature_high = scrapy.Field()
    temperature_low = scrapy.Field()
