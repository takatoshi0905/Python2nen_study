'''
取得した画像をフォルダに入れるプログラム
'''
import requests
from pathlib import Path

# 保存用フォルダをつくる
out_folder = Path("download")
#downloadフォルダを作成
out_folder.mkdir(exist_ok = True) 

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取りだして、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

# 画像データを、ファイルに書き出す
with open(out_path, mode = "wb") as f:
    f.write(imgdata.content)