from bs4 import BeautifulSoup
import lxml.etree as le

content_xml = le.HTML("news_0.html")
soup = BeautifulSoup(content_xml)
for div in soup.find_all(attrs={'class': 'left_zw'}):
    print('标签', div.name)
    print('标签名称', div.attrs)
    print('内容', div.string)