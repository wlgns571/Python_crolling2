# -*- coding:utf-8 -*-
# utf-8로
from bs4 import BeautifulSoup

import requests
movie_list = []
# for j in range(40):
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220516&page=1'\
      # +str(j+1)
resp = requests.get(url)
# print('status : ', resp.status_code)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(resp.text)
# print("구분"+ ("=" * 100))
print(soup.prettify()) # 구조화 출력

div = soup.select_one('.list_ranking')
# print(div)
#     trs = div.find_all('tr')
#
#     for i, v in enumerate(trs):
#         if i > 1:
#             if v.find('a'):
#                 try:
#                     no = v.select_one('td.ac:nth-child(1) > img').attrs['alt']
#                 except Exception as e:
#                     no = v.select_one('td.order').text
#                 try:
#                     arrow = v.select_one('td.ac > img.arrow').attrs['alt']
#                 except Exception as e:
#                     print(str(e))
#                 title = v.find('a').text
#                 img_url = v.find('a').attrs['href']
#                 score = v.select_one('td.range.ac').text
#                 movie_list.append([no, arrow, title, img_url, score])
# for i in movie_list:
#     print(i)
# # DB에서도 읽을수 있는 형식
# import csv
# with open('movie_score.csv', 'w', encoding='utf8') as f:
#     write = csv.writer(f, delimiter='|', quotechar='"')
#     for i in movie_list:
#         write.writerow(i)