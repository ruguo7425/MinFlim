# -*- coding: utf-8 -*-
import scrapy
import re
from TuShu.items import TushuItem


class TushuSpider(scrapy.Spider):
    name = 'tushu'
    allowed_domains = ['980ee.com']

    a_urls = "https://www.980ee.com/htm/movielist1/"
    start_urls = [a_urls + str(i) + '.htm' for i in range(1, 126)]
    print start_urls

    """
        href="/htm/movie1/9502.htm"
    """

    def parse(self, response):
        node_list = response.xpath("//ul[@class='movieList']/li")
        for node in node_list:
            item = TushuItem()
            item["url"] = 'https://www.980ee.com' + node.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url=item["url"], callback=self.parse_page
            )

    def parse_page(self, response):
        with open('index.html', 'w') as f:
            f.write(response.body)
        item = TushuItem()
        item['photo'] = "\n".join(response.xpath("//div[@class='poster']/img/@src").extract())
        item['name'] = "\n".join(response.xpath("//div[@class='poster']/img/@title").extract()).encode('utf8')
        bodyss = response.body
        s = 'http://666.maomixia666.com:888' + re.search(r'<.*?>.*\+(.*)\);</.*>', bodyss).group(1)
        s = re.sub('"', '', s)
        s = re.sub('\s', '', s)
        item['url'] = s
        yield item
        print item
