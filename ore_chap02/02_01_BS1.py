# インターネットにアクセスするライブラリをImport
import requests

# BeautifulSoupはbs4というライブラリに入っている
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)