from selenium import webdriver
browser = webdriver.Chrome()
url = 'https:www.baidu.com'
browser.get(url)
print(browser.page_source)
browser.close()