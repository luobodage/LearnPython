import requests
import lxml.etree as le

content1 = requests.get(
    url="http://www.xuexi.la/ziwojianding/74634.html",
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
).content

print(content1)
contentqx = le.HTML(content1)
for page in range(51,60):
    title = contentqx.xpath('//*[@id="contentText"]/p[{page}]/text()'.format(page=page))
    title_str = " ".join(title)
    with open('wendang.txt','a',encoding='utf-8') as f:
        f.write(title_str)