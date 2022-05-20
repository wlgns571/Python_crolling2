import json
import requests
from bs4 import BeautifulSoup
# 50개씩 36페이지까지
stock_list = []
for i in range(36):
    # url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=' + str(i+1) + '&pageSize=50'
    url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50'.format(i+1)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    jsonObj = json.loads(soup.text)
    stocks = jsonObj['stocks']

    for stock in stocks:
        stock_list.append([stock['itemCode'], stock['stockName'], stock['closePrice']])
if __name__ == '__main__':
    cnt = 0
    for i, v in enumerate(stock_list):
        print(v)
        cnt = cnt + 1
    print(cnt, '건')
    import csv
    with open('stock_list.csv', 'w', encoding='utf8') as f:
        write = csv.writer(f, delimiter='|', quotechar='"')
        for i in stock_list:
            write.writerow(i)
else:
    print("import other module")