import requests
import lxml.etree as le


def spider():
    content = requests.get(
        url='https://www.runoob.com/css/css-tutorial.html',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
    ).content

    # html转xml
    contentx = le.HTML(content)
    hrefs = contentx.xpath('//*[@id="leftcolumn"]/a/@href')

    for index, hrefs in enumerate(hrefs):
        url = 'https://www.runoob.com/' + hrefs
        detail_content = requests.get(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
            }
        ).content
        with open('%s.html' % index, 'wb') as f:
            f.write(detail_content)


if __name__ == '__main__':
    spider()
