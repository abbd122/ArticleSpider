# -*- coding: utf-8 -*-
import re

import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['http://top.jobbole.com']
    start_urls = ['http://top.jobbole.com/caijing/gsyw/89113/']

    def parse(self, response):
        body = response.body
        response_selector = response.xpath('//div')
        pass

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allow_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        teachers = response.xpath('//div[@class="li_txt"]')
        with open('/home/wangzheng/project/ArticleSpider/teacher.txt', 'w', encoding='utf-8') as file:
            for teacher in teachers:
                name = teacher.xpath('h3/text()').extract()[0]
                ty = teacher.xpath('h4/text()').extract()[0]
                content = teacher.xpath('p/text()').extract()[0]
                regex_str = '.*?([\u4E00-\u9FA5].*).*'
                name_obj = re.match(regex_str, str(name))
                ty_obj = re.match(regex_str, str(ty))
                if name_obj and ty_obj:
                    name = name_obj.group(1)
                    ty = ty_obj.group(1)
                    file.write('{}\t{}\t{}\n'.format(name, ty, content))
