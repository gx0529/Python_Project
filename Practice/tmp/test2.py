

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# searchTextBox = driver.find_element_by_id('kw')
searchTextBox = driver.find_element(By.ID, 'kw')
searchTextBox.send_keys("找到文本框")
time.sleep(3)
driver.quit()
