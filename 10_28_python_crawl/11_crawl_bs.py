# pip install bs4

from bs4 import BeautifulSoup as bs

html = """
<html>
 <head>
  <title>The Dormouse's story</title>
 </head>
 <body>
  <h1>this is h1 area</h1>
  <h2>this is h2 area</h1>
  <p class="title"><b>The Dormouse's story</b></p>
  <p class="story">Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
   <a class="brother" href="http://example.com/lacie" id="link2">Lacie</a>
   <a data-io="link3" class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
  </p>
  <p class="story">...</p>
 </body>
</html>
"""

# soup = bs(html, 'html.parser')

# # print('soup', type(soup))

# # 코드 정리(보기 좋게 정리)
# print('prettify', soup.prettify())

# # h1 태그에 액세스
# h1 = soup.html.body.h1

# print('h1 :', h1)

# # p 태그 액세스
# p1 = soup.html.body.p # 첫번째 매칭되는 것만 가져온다.
# print('p1 :', p1)

# # p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling
# p2 = p1.next_sibling.next_sibling
# print('p2 :', p2)

# # 텍스트 값 가져오기
# print("h1 : ", h1.string)

# # p1 텍스트 값 가져오기
# print("p : ", p1.string)

# # dir : 해당 객체의 변수와 함수(메서드)를 나열해준다.
# # print(dir(p2))

# print("p2 next : ", p2.next_element)
# # print("p2 next list: ", list(p2.next_element))


# select, select_one : css선택자
# find, find_all : 태그로 접근하여 속성을 사용

# find, find_all 명령
soup = bs(html, 'html.parser')

link1 = soup.find_all('a')

print(type(link1))

print(link1)

# link2 = soup.find_all("a", class_="sister")
link2 = soup.find_all("a", id="link2")
link2 = soup.find_all("a", string="Tillie")
link2 = soup.find_all("a", string=["Lacie","Tillie"])

print(link2)

# find는 처음 발견한 것만 가져옴
link3 = soup.find('a')
print('link3 : ', type(link3))
print(link3)

print(link3.string)
print(link3.text)

# 조건을 부여
link4 = soup.find("a", {"class": "sister", "data-io":"link3"})
link4 = soup.find("a", class_="brother")
print(link4)

# select, select_one

## select_one
# 태그 + 클래스 + 자식
link5 = soup.select_one("p.title > b")
print("link5 : ", link5)
print("link5 : ", link5.string)

# 태그 + id 선택자
link6 = soup.select_one("a#link1")
print("link6 : ", link6)

# 태그 + 속성
link7 = soup.select_one("a[data-io='link3']")
print("link7 : ", link7)

## select
link8 = soup.select("p.story > a")
print("link8 : ", link8)

link9 = soup.select("p.story > a:nth-of-type(2)")
print("link9 : ", link9)

link10 = soup.select("p.story")
print("link10 : ", link10)
print(link10[1])
print("========================")
for el in link10:
    temp = el.find_all("a")

    if temp:
        for v in temp:
            print(">>> ", v)
            print(">>> ", v.string)

    else:
        print(">>>", el)
        print(">>>", el.string)





