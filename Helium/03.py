from helium import *
import requests

sign_in_url = 'https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin#qrCodeLogin'
sign_on_url = 'https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex'

start_chrome(sign_in_url)

content = requests.get(
    url=sign_on_url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    },
    Cookie={
        '_uab_collina=159082210803006500676176; CASTGC=TGT-77588-yHgrHXIkcTdQe2Ztxpccdi1qM7rwBFW5iU7dS2wVXibHSfebIx-passport.zhihuishu.com; CASLOGC=%7B%22realName%22%3A%22%E9%99%88%E6%96%B0%E5%AE%87%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A182959539%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fapp%2Fcontent%2F201803%2F9f2de876645a4f9c81fddab77ce1e658_s3.png%22%2C%22uuid%22%3A%22EQWNMMrJ%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%22283c0d1882ef4018ae1e3e144b1b3ee7%22%7D; acw_tc=2f624a6e15985097357181890e405746b1176e8f58e7b5d737bca25423f1ac; exitRecod_EQWNMMrJ=2; SERVERID=58a6d0bed134adfd5bca4c165678e873|1598509741|1598509735; showDescription=success; u_asec=099%23KAFE7EEKE7MEhYTLEEEEEpEQz0yFD6fcDci4n6fHSuREW6tcSc97A6gcBYFET6i5EEwhE7TbDcdENba3U61vv0XBL5ZQSyO96KUt5Ram%2Fq8SroG3uz8sDzXnioZtSsJ8bLFtapw6rKrBrod3b6kWae7nCGrbApw5cRNE99r5rP2S6G%2FqQourAO7SwGCvaWh3byo69y%2Fmr6FnbUoRPz%2BdCRMZsYFET%2FyZTEwm%2BHGTEELStEw6GCfRdcGTE1LSt3llsyaSt3iSh3nP%2F3fXt37MlXZddqLStTLtsyaGQ3iSh3nP%2F3wYWEFE5U1sX6mq9HdpZGPluLFVJGApa88v0hw2aPgMXREYqMVI8mDNPvmUZVbpZCXgpBOonmUf2RSUf5OXZHgQb1EGLzA0JBWvyCT0DYAB6r5b06M6mSthE7Eht3BlluZdlYFETKxqAjJ5E7EFt37EFE%3D%3D'
    }
).content

click("形势与政策")

click('P40 《将改革进行到底》 党的自我革新')
