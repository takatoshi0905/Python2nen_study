'''
Yahoo!ニュースのトップをテキストファイルとして書き出すプログラム
本には書いていないけれど、ch1と合わせたらできそうな気がする
やってみよう。頑張ろうね。

2019/11/07
トップ、IT、サイエンスの各トップ記事をテキストファイルに出力するプログラムを作成。
ファイル名は「日時.txt」で、毎日もしくは毎時出力してもファイルが上書きされないようにした。
頑張ったね。

'''

import datetime
import requests
from bs4 import BeautifulSoup

# トップ記事の取得
load_url_topic = "https://news.yahoo.co.jp/"
html_top = requests.get(load_url_topic)
soup_top = BeautifulSoup(html_top.content, "html.parser")
topic_top = soup_top.find(class_ = "topicsList_main")

# IT関連記事の取得
load_url_IT = "https://news.yahoo.co.jp/categories/it"
html_IT = requests.get(load_url_IT)
soup_IT = BeautifulSoup(html_IT.content, "html.parser")
topic_IT = soup_IT.find(class_ = "topicsList_main")

# 科学関連記事の取得
load_url_sci = "https://news.yahoo.co.jp/categories/science"
html_sci = requests.get(load_url_sci)
soup_sci = BeautifulSoup(html_sci.content, "html.parser")
topic_sci = soup_sci.find(class_ = "topicsList_main")

# ファイル名の設定
# ファイル名は「年(2桁)+月+日+時間+分.txt」で出力する
# 出力フォルダは「ore_create」とする
now_dt = datetime.datetime.now()
filename = "ore_create/" + "{0:%y%m%d%H%M}".format(now_dt) + ".txt"

# ファイル書き込みモードで開く
# classで検索し、その中のすべてのaタグを検索して表示する
with open(filename, "w") as f:
    f.write("では、現在入っている主なニュースです。")
    f.write("\n\n----- トップ -----")
    for element in topic_top.find_all("a"):
        f.write("\n" + element.text)
    f.write("\n\n----- IT -----")
    for element in topic_IT.find_all("a"):
        f.write("\n" + element.text)
    f.write("\n\n----- サイエンス -----")
    for element in topic_sci.find_all("a"):
        f.write("\n" + element.text)
    f.write("\n\n\n...以上、ニュースをお伝えしました。")
