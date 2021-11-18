# requests 모듈 사용하기

import requests

# sess = requests.Session()

# res = sess.get("https://www.naver.com")

# print('1 : ', res.text)

# print(f'Status Code : {res.status_code}')

# # 상태코드를 이용해서 조건문에 활용할 경우
# print(f'상태코드 확인 : {res.ok}')

# sess.close()

# with requests.Session() as sess:
#     res = sess.get("http://daum.net")
#     print(res.text)
#     print(res.ok)


# httpbin.org 사이트는 HTTP Methods, Auth(인증), Status codes를 테스트
# 할 수 있는 사이트 중의 하나

sess = requests.Session()

res1 = sess.get('http://httpbin.org/cookies', cookies={"name": 'jhkim'})
print(res1.text)


res2 = sess.get('http://httpbin.org/cookies/set', cookies={"name": 'jhkim'})
print(res2)


# 가상의 User-Agent 
url = 'http://httpbin.org/get'
headers = {'user-agent': 'jhkim_app_v1.000_home_chrome'}

res3 = sess.get(url, headers=headers)

print(res3.text)

sess.close()



