from selenium import webdriver

url = 'https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl'

# 打開瀏覽器,確保你已經有chromedriver在你的目錄下
browser = webdriver.Chrome('./chromedriver')
# 在瀏覽器打上網址連入
browser.get(url)