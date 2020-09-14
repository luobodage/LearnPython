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
        content_xml_news = le.HTML(content_news)
        title = content_xml_news.xpath('//*[@id="cont_1_1_2"]/h1')
        text = content_xml_news.xpath('//*[@id="cont_1_1_2"]/div/p')

        with open('new1.txt','a+') as f:

            for index in range(len(title)):
                # links[index]返回的是一个字典
                if (index % 2) == 0:
                    print('标题：',title[index].text)
                    f.write('标题:' + title[index].text)
                    f.write('\r\n')

            for index in range(len(text)):
                # links[index]返回的是一个字典
                if (index % 2) == 0:
                    str_text = str(text[index].text)
                    for str_text_1 in str_text.split('None'):
                        print(str_text_1)
                        f.write(str_text_1)
                        f.write('\r\n')




if __name__ == '__main__':
    get_url()
