import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get("https://www.bilibili.com")
    content = r.content
    soup = BeautifulSoup(content, "lxml")
    title = soup.title.text
    print(title)