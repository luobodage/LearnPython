import requests
import lxml.etree as le


def spider():
    content = requests.get(
        url='https://blog.csdn.net/u014044812',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
    ).content

    # html转xml
    contentxt = le.HTML(content)
    hrefs = []
    titles = []
    for i in range(20):
        i += 1
        href1 = contentxt.xpath('//div[@id="mainBox"]/main/div[2]/div[%s]/h4/a/@href' % i)
        title1 = contentxt.xpath('//div[@id="mainBox"]/main/div[2]/div[%s]/h4/a/text()' % i)
        for href1 in href1:
            pass
        for title1 in title1:
            pass
        hrefs.append(href1)
        titles.append(title1)
    print(titles)

    for index, hrefs in enumerate(hrefs):
        url = hrefs

        detail_content = requests.get(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
            }
        ).content
        title = str(titles[index]).replace('\n', '').replace('\r', '').replace(' ', '')

        with open('csdn博客/%s.html' % title, 'wb') as f:
            f.write(detail_content)
        print("over")


if __name__ == '__main__':
    spider()
