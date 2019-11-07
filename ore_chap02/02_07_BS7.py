'''
ニュースの最新記事一覧を取得するプログラム
Yahoo!のトップニュースをとってこようね
試しにサイエンスニュースのトップもとってこようね
https://news.yahoo.co.jp/
https://news.yahoo.co.jp/categories/science
'''
import requests
from bs4 import BeautifulSoup

load_url_topic = "https://news.yahoo.co.jp/"
load_url_science = "https://news.yahoo.co.jp/categories/science"
html_top = requests.get(load_url_topic)
html_sci = requests.get(load_url_science)
soup_top = BeautifulSoup(html_top.content, "html.parser")
soup_sci = BeautifulSoup(html_sci.content, "html.parser")

# classで検索し、その中のすべてのaタグを検索して表示する
topic_top = soup_top.find(class_ = "topicsList_main")
topic_sci = soup_sci.find(class_ = "topicsList_main")

print("では、現在入っている主なニュースです。")
print("\n----- トップ -----")
for element in topic_top.find_all("a"):
    print(element.text)
print("\n----- サイエンス -----")
for element in topic_sci.find_all("a"):
    print(element.text)
print("\n...以上、ニュースをお伝えしました。")