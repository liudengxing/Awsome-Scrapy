# 爬取全国天气  


![python](https://img.shields.io/badge/language-python-green.svg?style=flat-square)![正常大小的矩形](https://img.shields.io/badge/IDE-atom-red.svg?style=flat-square)



天气爬虫 v1.0 

数据来源 [中国天气网]([http://www.weather.com.cn](http://www.weather.com.cn/))



#### 功能特性

- 爬取全国所有城市的天气信息数据



#### 运行

```
scrapy crawl weather_scrapy -o weather.xml
```

输出结果在本地目录下的 weather.xml

用 Excel 打开后可以另存为 xlsx



#### 更新日志

- 2019/08/20  实现全国天气爬取

- 2019/08/19  实现爬取以省份为单位的天气数据

- 2019/08/15  实现爬取单城市天气



#### TODO

- 全国天气选择爬取



#### Bug

- 爬取到的城市为不规律存储

