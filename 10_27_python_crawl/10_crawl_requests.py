# requests 모듈 사용하기

import requests

# sess = requests.Session()

# res = sess.get("https://www.naver.com")

# print('1 : ', res.text)

# print(f'Status Code : {res.status_code}')

# # 상태코드를 이용해서 조건문에 활용할 경우
# print(f'상태코드 확인 : {res.ok}')

# sess.close()

with requests.Session() as sess:
    res = sess.get("http://daum.net")
    print(res.text)
    print(res.ok)