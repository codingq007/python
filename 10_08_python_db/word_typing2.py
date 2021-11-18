import random
import time
import sqlite3
import datetime
import winsound


# DB 생성 & auto commit
conn = sqlite3.connect('../resource/records.db', isolation_level=None)

cursor = conn.cursor()

cursor.execute("create table if not exists records(id integer primary key autoincrement, cor_cnt integer, record text, regdate text)")

words = []

n=1 

cor_cnt = 0 # 정답 개수

# 문제 > word.txt에서 단어를 읽어와 words 리스트에 추가한 후 출력해보세요.
with open('../resource/word.txt', 'r') as fp:
    for word in fp:
        words.append(word.strip())

# print(words)   

# Enter 키가 눌릴 때까지 기다림.
input('게임 시작하려면, Enter키를 누르세요!!!')

start = time.time()

while n <=5:
    random.shuffle(words) # 섞는 역할
    q = random.choice(words) # 랜덤으로 하나를 뽑아옴.

    print()
    print(f'****** Question {n} *******')
    print(q)

    user_input = input() # 정답 입력

    # 정답 체크
    if str(q).strip() == str(user_input).strip():
        print('정답!!')
        # winsound.PlaySound('../resource/ding.wav', winsound.SND_FILENAME)
        
        cor_cnt += 1
    else:        
        print('땡!!!')

    n += 1 # 다음 문제로 전환

end = time.time()
etime = end - start # 총 게임시간
etime = format(etime, '.3f')

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# DB 기록
cursor.execute("insert into records('cor_cnt', 'record', 'regdate') values(?, ?, ?)", (cor_cnt, etime, datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')))

print(f'게임시간 : {etime} 초, 정답개수 : {cor_cnt}')        



















