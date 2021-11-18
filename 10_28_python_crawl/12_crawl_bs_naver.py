from bs4 import BeautifulSoup as bs
import requests as req

url="https://finance.naver.com/sise/lastsearch2.naver"

res = req.get(url)

# res.content(디코딩 되기 전), res.text(디코딩 후)

soup = bs(res.text, "html.parser")

# print(len(soup.select("table.type_5 tbody tr")))
print(len(soup.select("table.type_5 tr")))

# for tr in soup.select("table.type_5 tr")[2:]:
#     title = tr.select("a.tltle")[0]
#     print(len(title))
# for tr in soup.select("table.type_5 tr"):
#     if len(tr.select("a.tltle")) == 0:
#         continue
for tr in soup.select("table.type_5 tr:has(> .no)"):
    title = tr.select("a.tltle")[0].string.strip()
    price = tr.select("td.number:nth-child(4)")[0].string.strip()
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)

    print(title + "\t", price + "\t", change)

    