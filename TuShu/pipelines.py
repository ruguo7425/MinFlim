# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE
import os
import logging
# import re匹配


class TushuPipeline(object):
    def open_spider(self, spider):
        self.f = open('mingxing.txt', 'w')

    def process_item(self, item, spider):
        # 不能转换成中文.有错误,编码问题
        content = (json.dumps(dict(item)))
        self.f.write(content.encode())
        self.f.write('\n')

    def close_spider(self, spider):
        self.f.close()


class MinFlimImagesPipeline(ImagesPipeline):
    # 获取图片的管道  和获取数据的管道会冲突只能一个一个运行
    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        yield scrapy.Request(item['photo'])

    def item_completed(self, results, item, info):
        # print(results)

        # 原始图片保存路径
        source_path = IMAGES_STORE + [x["path"] for ok, x in results if ok][0]

        # 指定新的图片保存路径
        item["image_path"] = IMAGES_STORE + item["name"] + ".jpg"

        try:
            # 根据路径修改图片名 os.rename(old_name, new_name)
            os.rename(source_path, item["image_path"])
        except Exception as e:
            print(e)
            logging.error("Images %s rename failed" % source_path)

        return item
