import requests
import json
from bs4 import BeautifulSoup

def getData(url):
    res = requests.get(url, headers={
        'cookie' : 'over18=1'
    })
    root = BeautifulSoup(res.text, 'lxml')
    titles = root.find_all('div', class_='title')
    for title in titles:
        if title.a != None:
            print (title.a.string)

    nextlink = root.find('a', string = '‹ 上頁')
    return (nextlink['href'])

pageURL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count = 0
while count < 5 :
    pageURL = 'https://www.ptt.cc' +getData(pageURL)
    count += 1
