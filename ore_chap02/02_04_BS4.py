'''
すべてのタグを探して表示するプログラム
今回はliタグを検索して、その文字列を表示させる
以下のページからデータを取得する
https://www.ymori.com/books/python2nen/test2.html
'''

import requests
from bs4 import BeautifulSoup

# Webページを取得して解析
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):
    print(element.text)


