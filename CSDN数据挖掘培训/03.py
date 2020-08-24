import lxml.etree as le

def main():
    with open('cnjc.html','rb') as f:
        content = f.read()

    contentqx = le.HTML(content)
    titles = contentqx.xpath('//*[@id="leftcolumn"]/a/@title')

    for titles in titles:
        print(titles)

if __name__ == '__main__':
    main()