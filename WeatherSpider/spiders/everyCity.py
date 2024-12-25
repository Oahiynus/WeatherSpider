# -*- coding: utf-8 -*-
from re import findall
from urllib.request import urlopen
import scrapy
from ..items import WeatherspiderItem


class EverycitySpider(scrapy.Spider):
    name = "everyCity"
    allowed_domains = ["weather.com.cn"]
    start_urls = ["https://weather.com.cn"]

    def parse(self, response):
        pass
