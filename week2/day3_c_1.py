import urllib.request
url = 'https://i.pinimg.com/564x/b5/0a/17/b50a174bf010d09f0c61ea5a54ede8df.jpg'
saveNm = 'fcku.png'
urllib.request.urlretrieve(url, saveNm)
print('저장됨')
res = urllib.request.urlopen(url)
data = res.read()
text = data.decode('utf-8')
print(text)