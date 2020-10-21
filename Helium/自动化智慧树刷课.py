from helium import *

sign_in_url = 'https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin#qrCodeLogin'


def main():
    start_chrome(sign_in_url)

    click("形势与政策")

    click('继续学习')


if __name__ == '__main__':
    main()
