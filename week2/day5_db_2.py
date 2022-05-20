import json
import sqlite3
import requests
from bs4 import BeautifulSoup
from day5_s_5 import stock_list
conn = sqlite3.connect('./stock.db')
sql = """
    INSERT INTO stocks VALUES(?, ?, ?);
"""
# sql = """
#     INSERT INTO stocks VALUES(:code, :nm, :price);
# """
# list = [['1', 'a기업', 100],['2', 'b기업', 200],['3', 'c기업', 300]]
cur = conn.cursor()
# cur.execute(sql, {'code':1001, 'nm':'구글', 'price':9})
cur.executemany(sql, stock_list)
conn.commit()
cur.close()
conn.close()