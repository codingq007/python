
# 파이썬 흐름제어(제어문) 연습문제


# 1 ~ 5 문제 if 구문 사용

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# print(''.join([q1[s] for s in q1 if s == '가을']))
for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k, v in q1.items():
    if k == '가을':
        print(v)



# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

# q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
q2 = {"봄": "딸기", "여름": "토마토", "가을": "메론"}


for k, v in q2.items():
    if v == '사과':
        print(k, v)
        break
else:
    print("사과없음")    


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 88

if score >= 81:
    print('A학점')
elif score >= 61:    
    print('B학점')
elif score >= 41:
    print('C학점')    
elif score >= 21:
    print('D학점')    
else:
    print('E학점')    

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18
li = [12, 6, 18]

_max = a

if b > a:
    _max = b
if c > b:
    _max = c
print(_max)

max_n = li[0]
for n in li[1:]:
    if max_n < n:
        max_n = n

print('max_n :', max_n)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

if int(s[7]) % 2 == 0: # 1 또는 0
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]


# print(''.join([s for s in q3 if s != '정']))

for v in q3:
    if v == "정":
        continue
    else:
        print(v, end='')

# 리스트 컴프리헨션
q66 = [x for x in q3 if x != '정']
print(q66)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

# print(' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))
print()
for n in range(1, 100):
    if n % 2 != 0:
        print(n, end=',')

print()
# 리스트 컴프리헨션에는 if문을 포함시킬 수도 있음.
q77 = [x for x in range(1, 101) if x % 2 != 0]
print(q77)


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

# print([s for s in q4 if len(s) >= 5])
for v in q4:
    if len(v) >= 5:
        print(v, end=' ')


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print()
# print([s for s in q5 if s.islower()])
for v in q5:
    if v.isupper():
        continue
    else:
        print(v, end=' ')

# 다른 방법
for v in q5:
    if v.islower():
        print(v, end=' ')


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())
        
print("------------------------- 10번")
print([s.upper() if s.islower() else s.lower() for s in q5])
