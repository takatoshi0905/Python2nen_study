'''
タグを検索して、そこにある文字列だけを抽出するプログラム
ここでは、title, h2, liタグを検索して、その文字列を表示する
'''

import requests
from bs4 import BeautifulSoup

# webページの取得および解析
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# title, h2, liタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)
