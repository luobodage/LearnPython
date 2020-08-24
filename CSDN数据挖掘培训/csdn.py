import requests
import lxml.etree as le


def spider():
    content = requests.get(
        url='https://blog.csdn.net/',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
    ).content

    # html转xml
    contentx = le.HTML(content)
    hrefs = contentx.xpath('//h2/a/@href')

    print(hrefs)
    for hrefs in hrefs:
        print(hrefs)

    # for index, hrefs in enumerate(hrefs):
    #     url =  hrefs
    #     detail_content = requests.get(
    #         url=url,
    #         headers={
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    #         }
    #     ).content



if __name__ == '__main__':
    spider()
