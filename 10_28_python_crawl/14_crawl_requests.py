# REST API: GET, POST, DELETE, PUT(update), PATCH(update, modify) 

# URL을 통해서 자원의 상태정보를 주고 받는 모든 것을 의미
# URL은 거의 변화가 없고 method만 변화

# GET : www.store.com/books     : 도서를 전부 조회
# GET : www.store.com/books/id  : id에 해당하는 도서를 조회
# POST : www.store.com/books/   : 도서를 생성
# PUT : www.store.com/books/    : 도서를 수정
# DELETE: www.store.com/books/  : 도서를 삭제

import requests
from requests.api import patch

sess = requests.Session()

# 요청
# res = sess.get('https://api.github.com/events')

# # 수신 상태 체크(문제가 있을경우 예외 발생)
# res.raise_for_status()

# print(res.text)

# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'goodman', domain='httpbin.org', path='/cookies')


# 요청
res = sess.get('http://httpbin.org/cookies', cookies=jar)

print(res.text)

# post방식 요청
res = sess.post('http://httpbin.org/post', data={'id':'test1212', 'pw':'1212'}, cookies=jar)

print(res.text)
print(res.headers)


# post 방식 요청 2
data1 = {'name':'kim', 'value':'true'}
data2 = (('name','lee'), ('value','false'))

res = sess.post('http://httpbin.org/post', data=data1)
print(res.text)

# put 요청 : 데이터를 수정/삽입
res = sess.put('http://httpbin.org/put', data=data1)
print(res.text)

# delete 요청 
res = sess.delete('http://httpbin.org/delete')
print(res.text)

#jsonplaceholder

res = sess.delete('https://jsonplaceholder.typicode.com/posts/1')

print(res.ok)
print(res.text)
print(res.headers)

sess.close()






