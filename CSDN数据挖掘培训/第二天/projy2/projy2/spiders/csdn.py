import scrapy
import lxml.etree as le


class CsdnSpider(scrapy.Spider):
    name = 'csdn'

    # allowed_domains = ['']
    # start_urls = ['http:///']

    def start_requests(self):
        keyword = 'python'
        page_num = 10
        for page in range(1, page_num + 1):
            url = f'https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=&viparticle=&domain=&o=&s=&u=&l=&f='.format(
                page=page,
                keyword=keyword
            )
            yield scrapy.Request(
                url=url,
                callback=self.parse1,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                }
            )

    def parse1(self, response):

        hrefs = response.xpath('//dl[@class="search-list J_search"]/dt[1]/div[1]/a[1]/@href').extract()
        for href in hrefs:
            yield scrapy.Request(
                url=href,
                callback=self.parse2,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                }

            )
            print(href)

    def parse2(self, response):
        # contentx = le.HTML(response.body)
        # title = tool.xpath_one(contentx,'//h1[@id="articleContentId]//text()'),default
        titles = response.xpath('//h1[@id="articleContentId"]//text()').extract()
        texts = response.xpath('//div[@id="content_views"]//text()').extract()
        print(titles)
        for text in texts:
            text = str(text).replace('\'\n\'', '').replace('\r', '').replace(' ', '').replace('\n\n', '').replace('\n',
                                                                                                                  '')

            print(text)
