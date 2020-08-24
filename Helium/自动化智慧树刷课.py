from helium import *


start_chrome("https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
write("",TextField('请输入手机号'))
write("",TextField('请输入密码'))
press(ENTER)