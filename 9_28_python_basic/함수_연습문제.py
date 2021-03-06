# *** 함수 연습문제 ***

# 1. print(), sum(), range()와 같은 함수를 무슨 함수라고 하나요.


# 2. 함수를 정의하는 키워드를 쓰세요.


# 3. 주어진 input에 대해 의도된 output을 전달하는 역할을 하는 것을 프로그래밍에서는 무엇이라고 하나요?


# 4. 리스트, 튜플과 같은 원소의 개수를 output하는 함수명을 적으세요.


# 5. 함수에 전달되는 입력을 무엇이라고 하는지 아는대로 적으세요.


# 6. 매개변수를 지정하지 않을 경우, 지정된 기본값으로 대체되는데 이러한 인자를 무엇이라고 하나요?


# 7. 위의  문제에 해당하는 내장 함수의 예를 들어보세요.


# 8. 함수의 종료를 명시하는 키워드는 무엇인가요?


# 9. 위 문제의 키워드가 생략된 경우 반환값은 무엇인지 적으세요


# 10. 함수의 반환값은 어디로 리턴되나요?



# 11. 다음 중 틀린 표현은 몇 번째 인가요?
#   def test(a, b, c = 1)
#   def test(a, b = 1, c)
#   def test(a = 1, b = 1, c = 3)


# 12. 키워드 파라미터를 관례적으로 어떻게 표현하는지 직접 함수의 선언부를 작성해보세요
# (인수의 갯수는 고정되지 않음, 함수명은 임의로 정하세요)


# 13. 특정 코드 블록(함수 안)에서 선언된 변수를 무엇이라고 하나요?


# 14. 프로그램 종료 전까지 유지되는 변수를 무슨 변수라고 하나요?


# 15. 위와 같은 변수의 범위를 영어로 무엇이라고 하나요?



# 16. 파라미터를 튜플 형태로 전달하는 함수의 선언부를 작성해보세요. (인자의 갯수가 고정되지 않음, 함수명은 임의로..)



# 17. 두개의 입력을 받아 합, 차, 곱의 결과를 튜플로 동시에 반환하는 함수를 정의 하고 실행해보세요.



# 18. 다음과 같은 함수를 정의하고 실행해보세요.(조건문을 이용)
'''
    함수명 : return_fruit
    입력 : color
    기능 : 
           color가 red 이면 apple을 반환
           color가 yellow 이면 banana를 반환
           color가 green 이면 water melon을 반환
           위의 color가 아니면 I don't know를 반환    
'''

def return_fruit(color):
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'water melon'
    else:
        return "I don't know"

# 19. 위의 문제를 아래 예시된 딕셔너리를 이용하여 함수를 정의하세요.
# get(a, b)함수 이용, 첫번째 인자 a는 찾고싶은 key, 두번째 인자 b는 key값이 없을 때 리턴되는 값
'''
fruit_dic = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'water melon'
}
'''



# 20. 입력 값 보다 작은 Fibonacci 수열을 출력하는 함수를 작성하세요
# 함수명 : fibonacci
# 피보나치 수열 : 0번째 원소를 0, 1번째 원소를 1로 두고 시작하여, 다음 2번째 원소는 앞의 두수의 합 1(0+1)을 놓고,
#                3번째 원소는 앞의 두수의 합 2(1 + (0+1))을, 4번째 원소는 역시 앞의 두수의 합 3(1 + 2)을 배치하는 방식으로
#                나열되는 수열을 말한다.
#              e.g) 0, 1, 1, 2, 3, 5, 8, 13, 21, ....



# 21. 위의 문제에서 수열을 리스트에 출력하도록 함수를 수정하세요.


# 22. 인자의 갯수가 하나 또는 두개만 허용된다고 가정하고, 하나인 경우는 제곱을 두개인 경우에는 두수의 곱을 반환하는 
#     함수를 정의해보세요. 함수명(var_arg)


# 23. a, b 서로 다른 두수 중 큰 값을 출력하는 코드를 삼항연산자(조건부 표현식)를 이용하여 작성하세요.
a = 10
b = 100




# 24. 위의 문제를 default parameter와 파이썬 삼항 연산자(조건부 표현식)를 이용하여 함수를 정의하세요.
# 함수명 : default_arg



# 25. 람다함수의 키워드를 쓰세요.


# 26. 람다함수와 일반함수의 차이점에 대해서 간략히 정리해보세요.


# 27. 람다 함수가 유용하게 사용되는 2개의 함수를 적으세요.

,
# 28. 주어진 리스트에서 5(포함) ~ 10(포함)사이의 값을 출력하는 코드를 작성하는데
#     map, filter 함수 중 하나를 이용하여 작성하세요.
#     nums = [1,2,3,6,8,9, 10, 11, 13, 15]



# 29. map, filter 함수 중 하나를 이용하여 다음과 같이 369 게임에 맞게 코드를 작성하세요.
# [1, 2, '박수', 4, 5, '박수', 7, 8, '박수'] (1 ~ 10범위)
 


# 30. 위의 문제에서 범위를 1 ~ 20까지 했을 때 코드를 작성하세요. (find함수 사용)
# [1, 2, '박수', 4, 5, '박수', 7, 8, '박수', 10, 11, 12, '박수', 14, 15, '박수', 17, 18, '박수'] (1 ~ 20범위)
# find() : 문자열에서 해당 문자의 index를 반환, 만일 없으면 -1을 반환 
# e.g> 'abcde'.find('b') 실행 후 확인해보세요.



# 31. 리스트 컴프리핸션과 람다 함수를 이용하여 구구단을 가로로 출력하는 리스트를 만들어 보세요
# e.g> ['2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', ... ]



# 32. 다음 예시와 같이 학생의 수를 입력받아 학생의 점수와 평균, 평균과의 차이를 구하여 출력하는
# 프로그램을 구현하세요. (함수를 이용하여 구현하세요) 

# 참고 사항 : 전체적인 구현을 먼저 한 후 부분 부분 함수를 정의해보세요.

# 학생 수를 입력받는다.
# 학생의 점수는 리스트에 append() 함수를 이용하여 학생수 만큼 루프를 돌려 추가시킨다.
# 리스트의 평균을 구한다.
# 평균미만자 수 : 구한 평균 미만의 점수를 카운트 한다.(루프 활용)
# 반복문을 활용하여 출력한다.

''' [ 프로그램 실행 화면 ]

학생 수를 입력하세요 : 4

1번 학생의 점수 : 88
2번 학생의 점수 : 79
3번 학생의 점수 : 85
4번 학생의 점수 : 78
------------------------------
 번호 	 점수 	 평균과의 차이
------------------------------

   1 	  88 	 5.50

   2 	  79 	 -3.50

   3 	  85 	 2.50

   4 	  78 	 -4.50
------------------------------
전체 평균 :  82.5
------------------------------
평균 미만자 수 :  2
------------------------------

'''


# 수고하셨습니다.. ^^
