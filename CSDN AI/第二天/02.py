import requests

url = 'https://cn-hljheb-cmcc-bcache-05.bilivideo.com/upgcxcode/89/21/261852189/261852189-1-16.mp4?e' \
      '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1606881569' \
      '&gen=playurl&os=bcache&oi=1971861989&trid=4e66838165b444538dfb8fdf7bab9360h&platform=html5&upsig' \
      '=b8dd8f565a68e3af1d65fe0006e4d4d4&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,' \
      'platform&cdnid=40082&mid=27860107&logo=80000000 '

content = requests.get(
    url=url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
).content

with open('木鱼水心.mp4', 'wb') as f:
    f.write(content)
