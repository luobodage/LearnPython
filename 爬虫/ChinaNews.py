import requests
from bs4 import BeautifulSoup
import lxml.etree as le


def get_url():
    content = requests.get(
        url='http://www.chinanews.com/'
        , headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

        }
    ).content
    content_xml = le.HTML(content)

    href_all = content_xml.xpath('//*[@id="daodu"]/div/div/a/@href')

    # for href in href_all:
    #     url = "http:" + href
    #     print(type(url))
    for i, href_all in enumerate(href_all):
        content_news = requests.get(
            url='http:' + href_all,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
            }
        ).content
        content_xml = le.HTML(content)
        print(content_xml)

        soup = BeautifulSoup(content_news,fromEncoding='utf-8')
        print(soup)
        # for div in soup.find_all(attrs={'class': 'left_zw'}):
        #     print('标签', div.name)
        #     print('标签名称', div.attrs)
        #     print('内容', div.string)


if __name__ == '__main__':
    get_url()
