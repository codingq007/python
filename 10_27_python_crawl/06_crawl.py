import urllib.request
from urllib.parse import urlparse

url = "http://www.ytn.co.kr/"

res = urllib.request.urlopen(url)

print(f'type : {type(res)}')
print(f'geturl : {res.geturl()}')
print(f'status : {res.status}')
print(f'getcode : {res.getcode()}')
print(f'headers : {res.getheaders()}')
print(f'read : {res.read(200).decode("utf-8")}')
# print(f'parse : {urlparse("http://www.ytn.co.kr/?id=test&pw=1234")}')
print(f'parse : {urlparse("http://www.ytn.co.kr/?id=test&pw=1234").query}')

# ipify.org

api_url = "https://api.ipify.org/"

values = {
    'format' : 'json'
}

# values = {
#     'format' : 'text'
# }

params = urllib.parse.urlencode(values)
print(params)

url2 = api_url + "?" + params

print(f"요청 url2={url2}")


# url2=https://api.ipify.org/?format=text

# url2=https://api.ipify.org/?format=json
data = urllib.request.urlopen(url2).read()


# "https://api.ipify.org/" 에서 응답한 형식
# text 요청시
# txt = 175.203.68.13

# json 요청시
# txt = {"ip":"175.203.68.13"}

txt = data.decode("utf-8")
print(f'response : {txt}')


