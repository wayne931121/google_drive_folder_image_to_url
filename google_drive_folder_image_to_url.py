import urllib.parse
import urllib.request
import re
import argparse, sys
parser = argparse.ArgumentParser(description="Google雲端硬碟資料夾圖片轉成可以放置網站中的圖片連結 Google drive image to website url, Test on 2023.06.08 zh_TW.")
parser.add_argument("-url", "-u", help="輸入一個只有放圖片的公開Google雲端硬碟資料夾連結。 Please input a public google drive folder which only place images.", type=str, default="")
parser.add_argument("-single", "-s", help="輸入一個單一圖片的公開Google雲端硬碟連結。 Please input a public google drive single image link.", type=str, default="")
args = parser.parse_args()
folder_url = args.url
single_url = args.single
if not folder_url and not single_url: sys.exit()
def request(url, headers={}): #下載原始碼，Download Source Code。
    req = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode(encoding="utf-8")
    response.close()
    return data
def collect_id(i):
    dataID.append(i["id"])
    return None
def collect_name(i):
    dataName.append(i["name"])
    return None
regex = 'data-id="(?P<id>[^"]+)"'
regex_name = 'data-tooltip-align="[^"]*" data-tooltip-delay="\\d*" data-tooltip-unhoverable="true">(?P<name>[^<]+)<\\/div>'
regex_url_id = 'https:\\/\\/lh3.googleusercontent\\.com\\/drive-viewer\\/(?P<url_id>[^\\\\]+)\\\\u003d'
print("轉成的網頁圖片連結，最高提供1600畫素乘以1200畫素。")
if folder_url:
    response = request(folder_url)
    dataID = []
    dataName = []
    re.sub(regex, collect_id, response)
    re.sub(regex_name, collect_name, response)
    urls = []
    for i in range(len(dataID)):
        response = request("https://drive.google.com/file/d/{}/view".format(dataID[i]))
        url = re.search(regex_url_id, response)["url_id"]
        url = "https://lh3.googleusercontent.com/u/0/drive-viewer/{}=s1600".format(url)
        urls.append(url)
        print(dataName[i],":",urls[i])
else:
    response = request(single_url)
    url = re.search(regex_url_id, response)["url_id"]
    url = "https://lh3.googleusercontent.com/u/0/drive-viewer/{}=s1600".format(url)
    print(url)