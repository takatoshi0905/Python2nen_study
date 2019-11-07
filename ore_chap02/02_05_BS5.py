'''
IDで検索して、そのタグの中身を表示するプログラム
IDはそのページ内に１つしかない要素に使う。第一章、第二章、などの時につけたりする
今回は以下のテストページの第二章を取得することを目的とする
https://www.ymori.com/books/python2nen/test2.html
'''
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(id="chap2")
print(chap2)