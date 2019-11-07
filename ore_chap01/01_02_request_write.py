# 取得したWebページのソースをテキストファイルに書き込むプログラム
#requestsはpipでインストールしてきたインターネットにアクセスするための外部ライブラリ
import requests

# URLの取得
url = "https://www.ymori.com/books/python2nen/test1.html"

# Webページの取得
response = requests.get(url)

# 文字化けを防ぐための処置
response.encoding = response.apparent_encoding

file_name = "download.txt"

# ファイルを書き込みモードで開く
# mode="w"は書き込みモード。他にもいろいろなモードを指定可能。
# f = open(file_name, mode="w")

# # インターネットから取得したデータを書き込む
# f.write(response.text)

# # ファイルを閉じる
# f.close()

# ファイルを開いて、書き込んで、閉じるの処理を一度に行う処理。
# こっちだと閉じ忘れのエラーを防ぐことができる。
with open(file_name, mode="w") as f:
    f.write(response.text)