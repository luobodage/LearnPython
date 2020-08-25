import scrapy


class S1Spider(scrapy.Spider):
    name = 's1'

    # allowed_domains = ['']
    # start_urls = ['http:///']

    def start_requests(self):
        yield scrapy.Request(  # yield产生了就送出去
            url='https://www.runoob.com/html/html-tutorial.html',
            callback=self.parse1
        )

    def parse1(self, response):
        print(response.body)  # 打印网站的源码
