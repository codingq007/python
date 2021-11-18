import urllib.request
import urllib.parse

# RSS : 사이트에서 보내주는 소식지(정보제공을 위한 새소식)

# 행정 안전부 : https://www.mois.go.kr/

#"https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001"

rss_url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# print(params)

for query in params:
   param = urllib.parse.urlencode(query)
#    print(param) 

   # rss_url 완성하기
   url = rss_url + "?" + param

   print(url)

   # 요청해서 읽어오기
   res = urllib.request.urlopen(url).read()
   # print(res) # 디코딩이 안된 데이터

   # 가져온 데이터를 디코딩하기
   contents = res.decode('utf-8') 

   # 
   print("=================================================")
   print(contents)

