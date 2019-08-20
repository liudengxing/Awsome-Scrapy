import scrapy
from weather.items import WeatherPerHourItem

class WeatherPerHourScrapy(scrapy.Spider):
    name = "weather_perhour_scrapy"
    start_urls = ['http://www.weather.com.cn/weather/101010100.shtml'
                  'http://www.weather.com.cn/textFC/anhui.shtml']

    def parse(self, response):
        item = WeatherPerHourItem()
        weathers = response.xpath('//div[@id="7d"]')

        # Get info
        for weather in weathers:
            item['city'] = response.xpath('//div[@class='crumbs fl']/a[2]/text()').get()
            item['date'] = weather.xpath('./ul/li/h1/text()').get()
            item['weather'] = weather.xpath('./ul/li/p[@title]/text()').get()
            item['temperature_high'] = weather.xpath('./ul/li/p[@class="tem"]/span/text()').get()
            item['temperature_low'] = weather.xpath('./ul/li/p[@class="tem"]/i/text()').get()
            item['wind'] = weather.xpath('./ul/li/p[@class="win"]/i/text()').get()

            yield item
