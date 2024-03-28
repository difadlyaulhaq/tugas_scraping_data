from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
import time

option = webdriver.ChromeOptions()
option.add_argument("--headless")
service = Service('chromedriver.exe')

driver = webdriver.Chrome(service=service, options=option)

base_url = "https://www.ebay.com/e/row/pre-loved-watches?_pgn={}"

jumlah_halaman = 10
list_nama, list_gambar, list_harga, list_link, list_dilihat = [], [], [], [], []

for halaman in range(1, jumlah_halaman + 1):
    url = base_url.format(halaman)
    driver.get(url)
    time.sleep(3)  

    content = driver.page_source
    data = BeautifulSoup(content, 'html.parser')

    # Memeriksa apakah halaman berhasil dimuat
    if "pre-loved-watches" not in driver.current_url:
        print(f"Gagal memuat halaman {halaman}. Melanjutkan ke halaman berikutnya...")
        continue

    print(f"Scraping data dari halaman {halaman}")

    for area in data.find_all('div', class_="s-item__wrapper clearfix"):
        nama = area.find('h3', class_="s-item__title").get_text()
        gambar = area.find('img')['src']
        harga = area.find('span', class_="s-item__price").get_text()
        link = "https://ebay.com" + area.find('a')['href']
        dilihat = area.find('div', class_="NEGATIVE")
        if dilihat != None:
            dilihat = dilihat.get_text()

        list_nama.append(nama)
        list_gambar.append(gambar)
        list_harga.append(harga)
        list_link.append(link)
        list_dilihat.append(dilihat)

df = pd.DataFrame({'Nama': list_nama, 'Gambar': list_gambar, 'Harga': list_harga, 'Link': list_link, 'Dilihat': list_dilihat})
df.to_csv('watch3.csv', index=False)



driver.quit()
