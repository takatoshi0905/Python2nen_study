#requestsはpipでインストールしてきたインターネットにアクセスするための外部ライブラリ
import requests

# URLの取得
url = "https://www.ymori.com/books/python2nen/test1.html"

# Webページの取得
response = requests.get(url)

# 文字化けを防ぐための処置
response.encoding = response.apparent_encoding

# 取得したWebページのソースを出力
print(response.text)
