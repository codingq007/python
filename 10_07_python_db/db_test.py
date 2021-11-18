'''
SQLite : DB서버가 필요없는(DB서버 설치 불필요) 
임베디드 관계형 데이터베이스로 경량의 데이터베이스이다.
오픈소스 DB엔진이다.
서비스하는 어플리케이션 영역 내부에 공존하는 형태의 
데이터베이스이다.
모바일이나 임베디드 기기에서 많이 사용되며 
신뢰성이 높은 편이다.
'''

import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)

# nowDateTime = now.strftime('%Y-%m-%d')
nowDateTime = now.strftime('%y-%m-%d %H:%M:%S')
print('nowDateTime : ', nowDateTime)

# DB 생성
conn = sqlite3.connect('../resource/database.db', isolation_level=None)
print(type(conn)) # <class 'sqlite3.Connection'>

# Cursor 생성(연결, 바인딩)
cur = conn.cursor()
# print('type : ', type(cur))

# Data Type : numeric, integer(정수), real(실수), text(문자열), blob(Binary Large Object)

# 테이블 생성
cur.execute("create table if not exists user( id integer primary key, \
    username text, email text, tel text, \
    website text, reg_date text)")

# 데이터 삽입
cur.execute("insert into user values(1, '김말똥', 'test@naver.com', \
    '010-1234-1234', 'www.test.com',?)",(nowDateTime,))

cur.execute("insert into user values(2, '고길동', 'test@naver.com', \
    '010-1234-1234', 'www.test.com',?)",(nowDateTime,))

# 여러개의 데이터를 한꺼번 삽입하기
# executeMany를 이용한 삽입(튜플, 리스트)
user_list = (
    (3, 'kang', 'test@google.com', '010-1234-1234', 'www.kang.com', nowDateTime),
    (4, 'ko', 'test2@google.com', '010-1234-1234', 'www.ko.com', nowDateTime),
    (5, 'joo', 'test3@google.com', '010-1234-1234', 'www.joo.com', nowDateTime),
)

cur.executemany("insert into user(id, username, email, tel, website, reg_date) values(?,?,?,?,?,?)",user_list)



# 테이블의 전체 데이터를 삭제하기
# conn.execute('delete from user')

# 결과 확인하기
# print('user db deleted : ', conn.execute('delete from user').rowcount, '행')


# conn.commit()

# 접속해제(리소스 반납)
conn.close()










