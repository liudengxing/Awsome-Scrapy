import scrapy
# import re
from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = "weather_spider"
    header  = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
    }

    def start_requests(self):
        url = "http://www.weather.com.cn/textFC/beijing.shtml"
        yield scrapy.Request(url)


    def parse(self, response):

        # print(response.body)
        item = WeatherItem()

        # citys = response.xpath('//div[@class="conMidtab" and not(@style)]/div[@class="conMidtab3"]/table/tbody/tr')
        citys = response.xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr')

        print("\n flag1 \n")

        target = open("response.txt", 'wb+')
        target.write(response.body)

        target = open("citys.txt", 'w+')
        for single in citys:
            target.write(str(city) + "\n")

        for city in citys:
            print("\n flag2 \n")
            item['city'] = city.xpath('.//td[@width=83]/a/text()').get()
            print("city:" + item['city'])
            item['weather_morning'] = city.xpath('.//td[@width=89]/text()').get()
            item['weather_evening'] = city.xpath('.//td[@width=98]/text()').get()

            # handle wind info
            wind_morning_list = city.xpath('.//td[@width=162]').getall()
            for wind_morning in wind_morning_list:
                wind_morning_single = "".join(wind_morning.split())

                # remove HTML tag
                # wind_morning_single_matched = re.sub(r'<.*?>','',wind_morning_single)

                # item['wind_morning'] = wind_morning_single_matched
                item['wind_morning'] = wind_morning_single

            wind_evening_list = city.xpath('.//td[@width=177]').getall()
            for wind_evening in wind_evening_list:
                wind_evening_single = "".join(wind_evening.split())

                # remove HTML tag
                # wind_evening_single_matched = re.sub(r'<.*?>','',wind_evening_single)

                # item['wind_evening'] = wind_evening_single_matched
                item['wind_evening'] = wind_evening_single

            # get temperature from response
            item['temperature_high'] = city.xpath('.//td[@width=92]/text()').get()
            item['temperature_low'] = city.xpath('.//td[@width=86]/text()').get()

            print("\n flag3 \n")
            yield item
