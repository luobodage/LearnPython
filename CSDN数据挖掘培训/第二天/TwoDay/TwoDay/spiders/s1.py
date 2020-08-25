import scrapy
import lxml.etree as le


class S1Spider(scrapy.Spider):
    name = 's1'

    # allowed_domains = ['']
    # start_urls = ['http:///']

    def start_requests(self):
        yield scrapy.Request(  # yield产生了就送出去
            url='https://www.runoob.com/html/html-tutorial.html',
            callback=self.parse1,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
            }
        )

    def parse1(self, response):
        print(response.body)  # 打印网站的源码

        contentx = le.HTML(response.body)
        # hrefs = contentx.xpath('//*[@id="leftcolumn"]/a/@href')
        # titles = contentx.xpath('//*[@id="leftcolumn"]/a/@title')
        a_s = contentx.xpath('//*[@id="leftcolumn"]/a')
        for a in a_s:
            href = a.xpath('./@href')
            title = a.xpath("./@title")
            if title and href:
                title = title[0]
                href = href[0]
                url = 'https://www.runoob.com/' + href
                yield scrapy.Request(
                    url=url,
                    callback=self.parse2,
                    meta={'title': title},
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                    }
                )
            print(title, href)

    def parse2(self, response):
        title = response.meta.get('title')
        print("完成了 %s" % title)
        with open('download/%s.html' % title, 'wb') as f:
            f.write(response.body)

        # for index, hrefs in enumerate(hrefs):
        #     url = 'https://www.runoob.com/' + hrefs
        #     detail_content = requests.get(
        #         url=url,
        #         headers={
        #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        #         }
        #     ).content
        #
        #     title = titles[index]
        #     with open('下载/%s.html' % title, 'wb') as f:
        #         f.write(detail_content)
        #     print("over")
