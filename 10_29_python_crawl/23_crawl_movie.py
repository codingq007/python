# pip install pandas
# pip install openpyxl

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

# print(get_movie_point(1, 3))        

import pandas as pd
column = ['번호', '영화제목', '포인트', '작성자' ]
results = get_movie_point(1,3)

dataframe = pd.DataFrame(results, columns=column)
# print(dataframe)
dataframe.to_excel('./movie.xlsx', sheet_name='영화평점', index=False, startrow=0)



        

