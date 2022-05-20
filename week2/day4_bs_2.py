# -*- coding:utf-8 -*-
# utf-8로
from bs4 import BeautifulSoup

import requests
img_list = []
search = 'cat/'
url = 'https://pixabay.com/images/search/' + search
print(url)
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup.prettify()) # 구조화 출력

div = soup.select_one('div.container--SjIGV > div.inner--l_u2E > div.result--efirA > div.container--HcTw2')
print(div)
# trs = div.find_all('tr')
#
# for i, v in enumerate(trs):
#     if i > 1:
#         if v.find('a'):
#             try:
#                 no = v.select_one('td.ac:nth-child(1) > img').attrs['alt']
#             except Exception as e:
#                 no = v.select_one('td.order').text
#             try:
#                 arrow = v.select_one('td.ac > img.arrow').attrs['alt']
#             except Exception as e:
#                 print(str(e))
#             title = v.find('a').text
#             img_url = v.find('a').attrs['href']
#             score = v.select_one('td.range.ac').text
#             img_list.append([no, arrow, title, img_url, score])
# for i in img_list:
#     print(i)