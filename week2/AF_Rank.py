import json
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import util
from bs4 import BeautifulSoup
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
time.sleep(1)
driver.get('https://afevent2.afreecatv.com/app/rank/index.php?szWhich=viewer')

# print(soup.prettify())
# rankAll = []
ranLiNm = []
ranLiNum = []
ranUrl = []
for i in range(30):

    driver.execute_script("getRank({0})".format(i+1))
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    ranList = soup.select_one('#rank_list')
    ranNmList = ranList.select('strong.bj_nick')
    for ranNm in ranNmList:
        ranLiNm.append(ranNm.text)
    ranNumList = ranList.select('div.num > em')
    for ranNum in ranNumList:
        ranLiNum.append(ranNum.text)
    ranIdList = ranList.select('span.bj_id')
    for ranId in ranIdList:
        ranUrl.append('https://bj.afreecatv.com/{0}'.format(ranId.text))

# print(ranUrl)
# rankAll.append([ranLiNm, ranLiNum, ranUrl])
# print(rankAll)
with open('AF_rank.txt', "wt", encoding="utf-8") as f:
    for i in range(len(ranLiNm)):
        f.write((str(['Rk: ', ranLiNum[i], ' | Nm: ', ranLiNm[i], ' | Url: ', ranUrl[i]])+'\n').replace("', '", ""))

