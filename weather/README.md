# 爬取全国天气  

天气爬虫 v1.0 

数据来源 [中国天气网]([http://www.weather.com.cn](http://www.weather.com.cn/))



#### 运行 ：

```
scrapy crawl weather_scrapy -o weather.xml
```

输出结果在本地目录下的 weather.xml

用 Excel 打开后可以另存为 xlsx



#### 更新日志

v1.0

- 实现全国天气爬取

v0.1.1

- 实现爬取以省份为单位的天气数据
- 数据以 城市 、早间天气 、晚间天气 、早间风力 、晚间风力 、早间温度 、晚间温度 7个维度储存

v0.1.0

- 实现 爬取单城市天气



#### feature

- 全国天气选择爬取



#### bugs

- 爬取到的城市是混乱存储的

