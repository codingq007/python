import random
import time # 시간 측정
import os

# 출제 문장 리스트

WORD_LIST = [
    "python은 배우기 쉬운 언어 입니다.",
    "앞으로 크롤링강좌를 시작합니다.",
    "UTF-8은 유니코드를 8비트 기반으로",
    "저장하는 인코딩 방식입니다.",
    "random은 난수를 발생시키는 모듈입니다."
]

# 리스트 셔플(순서를 섞음)
random.shuffle(WORD_LIST)
current_count = 0

for q in WORD_LIST:
    os.system("cls")
    current_count += 1
    # time() 함수는 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 
    # 초단위로 반환
    start_time = time.time() 
    # print('start_time : ', start_time)
    user_input = str(input(q + '\n')).strip()

    end_time = time.time() - start_time

    if user_input == 'quit':
        print('게임 종료!!')
        break
    
    correct = 0
    # 입력한 문자열에서 문자 하나씩(인덱스 포함해서) 가져온다.
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]: # 입력한 각문자와 예문의 각문자를 비교하여 같으면 카운트한다.
            correct +=1

    q_len = len(q) # 예문 길이
    cor = correct / q_len * 100 # 정확도
    err = (q_len - correct) / q_len * 100 # 오타율
    speed = float(correct / end_time) * 60 # 유효타 / 작성시간 * 60
    # 1분에 100타 ---> 100/60 * 60

    print("속도 : {:0.2f} 정확도: {:0.2f}% 오타율 : {:0.2f}% ". format (speed, cor, err))
    os.system('pause')
