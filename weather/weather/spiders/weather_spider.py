import scrapy
from weather.items import WeatherPerHourItem

class WeatherPerHourScrapy(scrapy.Spider):
    name = "weather_perhour_scrapy"
    start_urls = ['https://tianqi.qq.com/']

    def parse(self, response):
        item = WeatherPerHourItem()
        weathers = response.xpath('//ol[@id="ls-weather-hour"]')

        # Get info
        for weather in weathers:
            item['time'] = weather.xpath('.//p[@class="txt-time"]/text()').get()
            item['weather'] = weather.xpath('.//img/@title').get()
            item['temperature'] = weather.xpath('.//p[@class="txt-degree"]/text()').get()

            yield item
