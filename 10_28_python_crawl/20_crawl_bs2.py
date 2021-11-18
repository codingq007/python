import requests as req
from bs4 import BeautifulSoup as bs


keyword = "자바강의"
# url ="https://search.naver.com/search.naver?where=blog&query={}".format(keyword)
url =f"https://search.naver.com/search.naver?where=blog&query={keyword}"

res = req.get(url)
soup = bs(res.text, "lxml")

# print(len(soup.select(".lst_total li.bx")))
for li in soup.select(".lst_total li.bx"):
    # print(li)
    # print(li.select("img"))

    # 이미지의 링크 주소 가져오기
    thumbnail = li.select("img")[0]["src"]

    title = li.select("div > div> a.api_txt_lines")[0]
    title_link = title['href']

    summary = li.select("div > div > div > div > a > div.api_txt_lines")[0].text
    print(thumbnail, title, title_link, summary)
    print("*"* 100)