# pip install bs4
import requests as req
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/marketindex'
res = req.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.find_all('a')
# for i in links:
#     print(i)
links = soup.find_all('img')
for i in links:
    print(i.attrs['src'])
