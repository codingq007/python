# 자료형 연습문제 

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print('1 :', len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('2 :','apple;orange;banana;lemon')


# 3. 화면에 * 기호 100개를 표시하세요.
star = '*'
print('3 :', star * 100)

print('3 :','*'*100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 문자형으로 변환해보세요.
print('4 :', int('30'))
print('4 :', float('30'))
print('4 :', str('30'))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
q_str ="Niceman"
print('5 :',q_str[4:7])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
sb = "Strawberry"
print('6 :', sb[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
pNum = "010-7777-9999"
print('7 :',pNum[0:3]+pNum[4:8]+pNum[9:13])

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
url = "http://daum.net"
urlIdx = url.index('http://')
print(urlIdx)

print(url[urlIdx + 7:])
print('8 :', url[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
_str = "NiceMan"
print(_str.upper())
print(_str.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
str = "abcdefghijklmn"
print(str[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
_list = ["Banana", "Apple", "Orange"]
_list.remove("Apple")
print(_list)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tup = (1,2,3,4)
list(tup)

print([s for s in tup])
# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

#dic = {
#  '성인' :100000,
#  '청소년' : 70000,
#  '아동' : 30000
#}



dic = {}
dic['성인'] = 100000
dic['청소년'] = 70000
dic['아동'] = 30000

print(dic)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dic['소아'] = 0
print(dic)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(dic.keys())
print(list(dic.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(dic.values())
print(list(dic.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        