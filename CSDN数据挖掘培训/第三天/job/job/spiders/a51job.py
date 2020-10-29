import scrapy
import re
import json
import pymongo

c = pymongo.MongoClient().get_database("2020-10-29").get_collection('c2')


class A51jobSpider(scrapy.Spider):
    name = '51job'

    # allowed_domains = ['']
    # start_urls = ['http:///']

    def start_requests(self):
        page_num = 10
        keyword = 'python'
        for page in range(1, page_num):
            url = 'https://search.51job.com/list/220200,000000,0000,00,9,99,{keyword},2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(
                keyword=keyword,
                page=page
            )
            yield scrapy.Request(
                url=url,
                callback=self.parse1,
            )

    def parse1(self, response):
        content_str = response.body.decode('gbk', 'ignore')
        rets = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', content_str)
        rets1 = [str(i) for i in rets]
        rets2 = ' '.join(rets1)  # list转str
        print(rets2)
        print(type(rets2))
        d = json.loads(rets2)

        results = d['engine_search_result']
        c.insert_many(results)
        print("完成")
        gen = c.find()  # 数据生成器
        for data in gen:
            print(data)
