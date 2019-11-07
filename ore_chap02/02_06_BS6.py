'''
IDを指定し、その中のliタグを文字列として出力する
以下のサイトからデータを取得
第２章の文字列を取得できる
https://www.ymori.com/books/python2nen/test2.html
'''

import requests
from bs4 import BeautifulSoup

# webページの取得と解析
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索し、その中のすべてのliタグを検索して表示する
# IDが「chap2」を検索
chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
    print(element.text)
