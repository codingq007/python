import sqlite3

# DB 접속
conn = sqlite3.connect('../resource/database.db')

# cursor 바인딩
cur = conn.cursor()

# 데이터 수정 1
# cur.execute("update user set username = '홍길동' where id = 2")
# cur.execute("update user set username = ? where id = ?", ('홍길남', 3))

# 문제 > ID가 1번인 고객의 이름과, 전화번호, EMAIL을 수정하세요...
# 이름: 손흥민, 1111111,  son@naver.com
# cur.execute("update user set username = '홍길동', tel = '1111', email = 'son@naver.com' where id = 1")
# cur.execute("update user set username = ?, email=?, tel=? where id = ?", ('홍길서','son@naver.com', '1111', 3))

# 데이터 수정 2
# cur.execute("update user set username = '%s' where id = '%s'" % ('kang2', 4))
# f스트링 이용하기
# cur.execute(f"update user set username = '{'강길동'}' where id = {4}")

# 데이터 수정 3
# cur.execute("update user set username = :name where id = :id", {'name':'고길동', 'id':5})

# # 문제 > 데이터 확인하세요.. 반복문
# for user in cur.execute('select * from user'):
#     print(user)

# # 데이터 삭제 1
cur.execute("delete from user where id = ?",(2,))

# # 데이터 삭제 2
cur.execute("delete from user where id = :id", {'id':5})

# # 데이터 삭제 3
cur.execute("delete from user where id = '%s'" % 4)

# # 남은 데이터 모두 지우기(삭제된 행의 수 출력하기)
# print('삭제 : ', cur.execute("delete from user").rowcount, '행')
# # print('삭제 : ', conn.execute("delete from user").rowcount, '행')



conn.commit()
conn.close()