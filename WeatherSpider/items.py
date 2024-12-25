# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    scrapy.Field() 
    city = scrapy.Field() # 城市
    date = scrapy.Field() # 日期
    week = scrapy.Field() # 星期几
    weather = scrapy.Field() # 天气
    minTempeture = scrapy.Field() # 最低温度
    maxTempeture = scrapy.Field() # 最高温度
    wind = scrapy.Field() # 风向
    pass