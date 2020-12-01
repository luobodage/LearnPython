import requests
import json
"""

为什么这个就会有json错误

https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery351037809910486827936_1606457713746&_=1606457713747
"""
# url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery351037809910486827936_1606457713746&_=1606457713747'

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
response = requests.get(
    url=url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
).json()

data = json.loads(response['data'])
with open('世界疫情数据.json', 'w') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=2))

