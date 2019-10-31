from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

browser5 = Chrome()
browser5.get("https://www.momoshop.com.tw/main/Main.jsp")

element5 = browser5.find_element_by_id("keyword")
element5.clear()
element5.send_keys("寶可夢")
element5.send_keys(Keys.RETURN)
time.sleep(5)
area = browser5.find_elements_by_class_name("listArea")
print(type(area), len(area))
products = area[0].find_elements_by_class_name("goodsUrl")
print("momo searched %d goods"%len(products))
for p in products:
    print(p.get_property("href"))
    productName = p.find_element_by_class_name("prdName")
    print(productName.text)
    priceNumber = p.find_element_by_class_name("price")
    print(priceNumber.text)