import sqlite3

# DB 연결
conn = sqlite3.connect('../resource/database.db')

# 커서 바인딩
cur = conn.cursor()

# 데이터 조회하기
cur.execute('select * from user')

# # 레코드(행) 하나 가져오기
# print('1 : \n', cur.fetchone())

# # 지정한 수만큼 레코드(행) 가져오기
# print('2 : \n', cur.fetchmany(2))

# # 전부 가져오기
# print('ALL : \n', cur.fetchall())

# # 현재 cursor위치에서는 더이상의 행이 없기 때문에 빈 리스트값 반환
# print('ALL : \n', cur.fetchall())

print('------------------------')

# 반복문 사용하기 1
# rows = cur.fetchall()

# for row in rows:
#     print('조회 : ', row)

# 반복문 사용 2
# for row in cur.fetchall():
#     print('조회2 : ', row)    

# 반복문 사용 3
# cur.execute('select * from user')
# for row in cur.execute('select * from user'):
#     print('조회3 : ', row)

print('---------- where 패턴 -------------')
# # where절 패턴 1
# param1 = (2,)
# cur.execute("select * from user where id = ?", param1)
# print('param1 : ', cur.fetchone())

# # 현재 위치에서는 더이상 레코드가 없음. 빈리스트 반환
# print('param1 :', cur.fetchall())

# # where 절 패턴 2
# param2 = 3
# # cur.execute('select * from user where id="%s"' % param2)
# cur.execute(f'select * from user where id={param2}')

# print('param2 : ', cur.fetchone())
# print('param2 : ', cur.fetchall())

# # where 절 패턴3
cur.execute('select * from user where id=:id', {'id': 4})
print('param3 : ', cur.fetchone())
print('param3 : ', cur.fetchall())

# # where 절 패턴4
param4 = (2,5)
cur.execute('select * from user where id in(?,?)', param4)
print('param 4 : ', cur.fetchall())

# # where 절 패턴5
cur.execute("select * from user where id in('%d', '%d')" %(3,4))
print('param5 : ', cur.fetchall())

# where 절 패턴6
cur.execute('select * from user where id=:id1 or id=:id2', {'id1':2, 'id2':5})
print('param6 :', cur.fetchall())

# # db backup : dump 파일 만들기

# # with구문 이용시 fp.close(), conn.close() 자동 호출
# with conn:
#     with open('../resource/dump.sql', 'w') as fp:
#         for line in conn.iterdump():
#             fp.write('%s\n' % line)
#         print('Dump 작성 완료!!')

conn.close()











