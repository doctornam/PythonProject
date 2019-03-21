'''
pip install request beautifulsoup4 lxml
'''

import requests 
from bs4 import BeautifulSoup
import time
import json

KAKAO_TOKEN = "카카오토큰 입력"
send_lists = []

def send_to_kakao(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def search_slickdeals(condition):
    keyword = condition["keyword"]
    min_price = condition["min_price"]
    max_price = condition["max_price"]

    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&searcharea=deals&searchin=first".format(keyword)
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "lxml")
    divs = bs.select("div.resultRow") # select 의 결과는 리스트이다.

    for d in divs:
        images = d.select("img.lazyimg")[0] # select 의 결과는 리스트이다.
        image = images.get("data-original")
        alink = d.select("a.dealTitle")[0]
        href = "https://slickdeals.net" + alink.get("href")
        title = alink.text
        price = float(d.select("span.price")[0].text.replace("$", "").replace("Free", "0"))
        fire = len(d.select("span.icon-fire"))
        
        if min_price < price <= max_price:
            send = True
            for s in send_lists:
                if s["title"] == title:
                    print("보낸적 있음")
                    send = False

            if send:        
                text = "{} {} {} {}".format(title, price, fire, href)
                r = send_to_kakao(text)
                print(r.text)
                send_lists.append({
                    "title": title,
                    "price": price,
                    "fire": fire,
                    "href": href,
                })

if __name__ == "__main__":
    condition = {
        "keyword": "apple ipad",
        "min_price": 100,
        "max_price": 250,
    }

    while True:
        search_slickdeals(condition)
        time.sleep(60 * 5)