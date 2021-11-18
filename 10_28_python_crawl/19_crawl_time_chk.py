from bs4 import BeautifulSoup as bs
import requests as req
import time

def chk_time(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() -start_time

        print(f"함수 {func.__name__} 동작시간 : {end_time}")
        return result
    return inner_func

url="https://finance.naver.com/sise/lastsearch2.naver"


@ chk_time
def r_select(url, parser):
    res = req.get(url)

    soup = bs(res.text, parser)

    titles = []
    for tr in soup.select("table.type_5 tr:has(> .no)"):
        title = tr.select("a.tltle")[0].string.strip()
        # price = tr.select("td.number:nth-child(4)")[0].string.strip()
        # change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
        titles.append(title)

    return titles
        

r_select(url, "html.parser")        
r_select(url, "lxml")        