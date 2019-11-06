import requests

url = "https://www.ymori.com/books/python2nen/test1.html"

response = requests.get(url)
response.encoding = response.apparent_encoding
print(response.text)

# 確認用のコメント 
# 結局、新しいフォルダつくって、そこに入れて接続し直すことにした。