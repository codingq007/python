import requests as req
from bs4 import BeautifulSoup as bs

for i in range(1, 10):
    url ="https://movie.naver.com/movie/point/af/list.naver?&page={i}"

    res = req.get(url)
    soup = bs(res.text, "lxml")

    trs = soup.select('table.list_netizen > tbody > tr')

    # print(len(trs))

    for tr in trs:
        tds = tr.select("td")

        number = tds[0].text
        title = tds[1].select("a")[0].text
        point = tds[1].select("div em")[0].text
        writer = tds[2].select("a")[0].text 

        
        # 태그 및 태그 의 내용 모두 제거
        # [x.extract() for x in tds[1].select('a')]
        # [x.extract() for x in tds[1].select('div')]
        # [x.extract() for x in tds[1].select('br')]

        # content = tds[1].text.strip()

        content = tds[1].select_one('br').next_sibling.strip()

        print(number, title, point, writer+'\n', 'review : '+content+'\n')

