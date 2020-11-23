import requests


def spider_jd():
    # 爬取京东商品页
    url = 'https://www.runoob.com/'
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text[:2000])
    except:
        print('爬取失败')


if __name__ == '__main__':
    spider_jd()
