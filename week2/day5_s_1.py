#pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('./chromedriver')
# 웹 자원 로드를 위해 3초 기다리기
driver.implicitly_wait(3)
driver.get(url)

driver.find_element_by_id('SearchGNBText').send_keys('대만')
driver.find_element_by_css_selector('button.search-btn').click()
time.sleep(3)
lis = driver.find_elements_by_css_selector('ul.boxList li.boxItem ')
for li in lis:
    # print(li.get_attribute('innerHTML'))
    print(li.find_element_by_css_selector('h5.infoTitle').text)
    print(li.find_element_by_css_selector('strong').text)
driver.stop_client()
driver.close()


