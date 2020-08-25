import requests


def main():
    content = requests.get(
        # url='https://blog.csdn.net/',
        url='https://www.baidu.com/'
                           ).content
    with open('baidu.html', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    main()
