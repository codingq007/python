# 문제> sbs 정치, 경제, 사회, 연예 rss 사이트 내용을 스크랩 하세요.

'''
정치 : https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01&plink=RSSREADER
경제 : https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=02&plink=RSSREADER
사회 : https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=03&plink=RSSREADER
연예/방송 : https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=14&plink=RSSREADER

'''
import urllib.request
import urllib.parse
rURL = "https://news.sbs.co.kr/news/SectionRssFeed.do"

params = []

for query in ['01', '02', '03', '14']:
    params.append(dict(sectionId=query))

# print(params)    

for c in params:
    param = urllib.parse.urlencode(c)

    url = rURL + "?" + param + "&plink=RSSREADER"

    res_data = urllib.request.urlopen(url).read()

    contents = res_data.decode("utf-8")
    print("====================================")
    print(contents)