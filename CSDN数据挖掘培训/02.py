import requests


def main():
    content = requests.get(
        url='https://www.runoob.com/html/html-tutorial.html',
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
    ).content
    with open('cnjc.html','wb') as f:
        f.write(content)
    # print(content)


if __name__ == '__main__':
    main()
