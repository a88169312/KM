from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome = "C:\chrome\chromedriver.exe"
driver = webdriver.Chrome(chrome)
driver.implicitly_wait(3)                               #瀏覽器等待時間
driver.get("https://www.python.org/")     #driver讀取的網址
assert "Python" in driver.title
element = driver.find_element_by_name("q")
element.clear()
element.send_keys("pytorch")
element.send_keys(Keys.RETURN)



