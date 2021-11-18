import requests as req
from bs4 import BeautifulSoup as bs
import csv

def get_movie_point(start, end):

    results = []

    for i in range(start, end+1):
        url ="https://movie.naver.com/movie/point/af/list.naver?&page={i}"

        res = req.get(url)
        soup = bs(res.text, "lxml")

        trs = soup.select('table.list_netizen > tbody > tr')
        for tr in trs:
            tds = tr.select("td")

            number = tds[0].text
            title = tds[1].select("a")[0].text
            point = tds[1].select("div em")[0].text
            writer = tds[2].select("a")[0].text 

            results.append([number, title, point, writer])
        return results

print(len(get_movie_point(1, 3)))        

results = get_movie_point(1, 3)

# with open('./movie_avg.csv', 'w', encoding="utf-8") as f:
with open('./movie_avg.csv', 'w', encoding="utf-8", newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(results)

        

