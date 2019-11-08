'''
ほぼ日刊イトイ新聞の「今日のダーリン」を取得するプログラム
毎日、イトイさんのコラムをこれで読む。
やってみよう。頑張ろうね。
'''
import datetime
import requests
from bs4 import BeautifulSoup

# ダーリンの取得
load_url_1101 = "https://www.1101.com/home.html"
html_1101 = requests.get(load_url_1101)
soup_1101 = BeautifulSoup(html_1101.content, "html.parser")
topic_1101 = soup_1101.find(class_ = "darling__txt")

# ファイル名の設定
# 出力フォルダは「ore_create」とする
now_dt = datetime.datetime.now()
filename = "ore_create/" + "今日のダーリン" + "{0:%y%m%d}".format(now_dt)  + ".txt"

# ファイル書き込みモードで開く
# classで検索し、その中のすべてのpタグを検索して表示する
with open(filename, "w") as f:
    f.write("今日のダーリン")
    for element in topic_1101.find_all("p"):
        f.write("\n" + element.text)