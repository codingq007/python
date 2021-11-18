# 문제> google 검색해서 타이틀과 내용을 크롤링하여 50 ~ 60개 데이터를
# 몽고 DB에 저장하세요.
# 필드 : name, title, contents, regdate, hit ( name : 아무개)

# DB 테스트 자료 만들기 위한 크롤링
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient, collection
from datetime import datetime

client = MongoClient(host="localhost", port = 27017)
db = client.webtest
collection = db.board

# https://www.google.com/search?q=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC&start=30

header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

for i in range(2):
    url = "https://www.google.com/search?q={}&start={}".format("투수", i*10)
    res = requests.get(url, headers=header)

    bs = BeautifulSoup(res.text, "lxml")

    lists = bs.select("div.tF2Cxc")
    # print(len(lists))

    for li in lists:
        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        try:
            title = li.select_one("h3.LC20lb.DKV0Md").text
            # print(title)
            contents = li.select_one("div.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf").text
            # print("컨텐츠 : ", contents)

            collection.insert_one({
                "name":"아무개",
                "title":title,
                "contents":contents,
                "regdate":current_utc_time,
                "hit":0
            }) 
        except:
            pass






