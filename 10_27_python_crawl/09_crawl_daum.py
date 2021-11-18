# pip install fake_useragent
import json
import urllib.request as req
from fake_useragent import UserAgent

vua = UserAgent()

print(vua.ie)
print(vua.chrome)
print(vua.safari)
print(vua.msie)
print(vua.random) # 랜덤하게 user-agent를 바꾸면서 생성

# 직접 접근하면 403 forbidden 에러 
# https://finance.daum.net/api/search/ranks?limit=10

# 가상의 헤더를 만들기
headers = {
    'User-agent':vua.ie,
    # 이전에 어디서 왔는지를 의미하는 헤더
    'referer':'https://finance.daum.net/'
}

# 요청 URL
url = 'https://finance.daum.net/api/search/ranks?limit=10'

# 요청헤더를 추가해서 요청을 해야한다.
# 이때 Request클래스를 이용한다.
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# res 데이터는 json Data
# print('res : ', res)

print('------------------------')
# 수신된 데이터(str)를 json으로 변환
# data키에 대한 value 가져오기
rank_data = json.loads(res)['data']

print('주식 인기 순위 데이터 : ', rank_data, '\n')

for stock_rank in rank_data:
    # print(type(stock_rank))
    print(f'순위:{stock_rank["rank"]}, 종목명:{stock_rank["name"]}, 현재가:{stock_rank["tradePrice"]}')




