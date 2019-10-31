import requests
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
import time, re
from PIL import Image
from urllib import request

chrome = "C:\chrome\chromedriver.exe"                   #deiver.exe的路徑
driver = webdriver.Chrome(chrome)                       #開啟Chrome driver
driver.implicitly_wait(3)                               #瀏覽器等待時間
driver.get("https://www.instagram.com/real__yami/")     #driver讀取的網址
allresult =[]
finalresult =[]

for i in range(9):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "lxml")
    #print(soup.prettify())
    html = etree.HTML(soup.prettify())                      #將soup.prettify經過etree.HTML的處理 做使用xpath的準備
    result = html.xpath("//img[@class='FFVAD']/@src")       #使用xpath找尋網頁特定標籤位置內容
    allresult += result
    #print(result[1])

print(len(allresult))

for item in allresult:
    if not item in finalresult:
        finalresult.append(item)
print(len(finalresult))

for i in range (len(finalresult)):
    print(finalresult[i])
    file1 = request.urlopen(finalresult[i])
    image1 = Image.open(file1)
    image1.save('Images\\Image%d.jpg'%i)


driver.close()

'''
太神啦!! 輸入使用者ID 抓取圖片網址
'''