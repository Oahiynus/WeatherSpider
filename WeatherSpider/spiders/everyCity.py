import scrapy
# -*- coding: utf-8 -*-
from re import findall
from urllib.request import urlopen
import scrapy
from ..items import WeatherspiderItem

'''
class EverycitySpider(scrapy.Spider):
    name = "everyCity"
    allowed_domains = ["weather.com.cn"]
    start_urls = ["https://weather.com.cn"]

    def parse(self, response):
        pass 
'''

class EverycityinsdSpider(scrapy.Spider):
    name = 'everyCity'

    allowed_domains = ['www.weather.com.cn'] 
    start_urls = []
    # 遍历各城市，获取要爬取的页面 URL
    url = r'http://yn.weather.com.cn/' 
    with urlopen(url) as fp:
        contents = fp.read().decode()

    pattern = '<a title=".*?" href="(.+?)" target="_blank">(.+?)</a>' 
    for url in findall(pattern, contents):
        start_urls.append(url[0])
    
    def parse(self, response):
        # 处理每个城市的天气预报页面数据
        item = WeatherspiderItem()

        city = response.xpath('//div[@class="crumbs fl"]//a[2]//text()').extract()[0] 
        item['city'] = city

        # 每个页面只有一个城市的天气数据，直接取[0]
        selector = response.xpath('//ul[@class="t clearfix"]')[0]

        # 存放天气数据
        weather = ''

        for li in selector.xpath('./li'):
            date = li.xpath('./h1//text()').extract()[0]
            cloud = li.xpath('./p[@title]//text()').extract()[0]
            temps = li.xpath('./p[@class="tem"]//span//text()').extract()
            if temps:
                high = temps[0]
            else:
                high = "No data available"  # 或者其他适当的默认值 
            low = li.xpath('./p[@class="tem"]//i//text()').extract()[0]
            wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0] 
            wind = wind + li.xpath('./p[@class="win"]//i//text()').extract()[0]
            
            weather = weather + date+':'+cloud+','+high+r'/'+low+','+wind+'\n' 
        
        item['weather'] = weather
        return [item]