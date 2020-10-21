from helium import *


def Web_start():
    name = input("请输入你要搜索的物品:")
    start_chrome("https://www.jd.com/")
    press(ENTER)


if __name__ == '__main__':
    Web_start()
