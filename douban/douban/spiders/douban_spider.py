import scrapy
from douban.items import DoubanItem

class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url)


    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['number'] = movie.xpath(".//div[@class='pic']/em/text()").get()
            item['title'] = movie.xpath(".//span[@class='title']/text()").get()
            item['rating_num'] = movie.xpath(".//span[@class='rating_num']/text()").get()
            item['rating_person'] = movie.xpath(".//div[@class='star']/span[4]/text()").get()

            # 获取简略信息
            content_list = movie.xpath(".//div[@class='bd']/p[1]/text()").getall()
            for content in content_list:
                content_single = "".join(content.split())
                item['introduce'] = content_single

            item['describe'] = movie.xpath(".//div[@class='bd']/p[2]/span[1]/text()").get()

            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').get()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield scrapy.Request(next_url)
