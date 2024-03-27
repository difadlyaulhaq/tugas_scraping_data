from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
import time

option = webdriver.ChromeOptions()
option.add_argument("--headless")
servis = Service('chromedriver.exe')

driver = webdriver.Chrome(service=servis,options=option)

url = "https://www.ebay.com/e/row/pre-loved-watches"
driver.set_window_size(1300,800)
driver.get(url)
time.sleep(5)
driver.save_screenshot("ebay_watches.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content,'html.parser')
print(data.encode("utf-8"))
i = 1
for area in data.find_all('div', class_="s-item__wrapper clearfix"):
    print(i)
    print(area)
    i += 1
    print("-------------")
