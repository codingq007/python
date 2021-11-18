import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

sql = """
    create table if not exists board(
        'id' integer primary key autoincrement,
        'writer' varchar(50),
        'title' varchar(200),
        'contents' text
    )
"""

cur.execute(sql)

# sql = "insert into board('writer', 'title', 'contents') values('홍길동', '안녕하세요', '반갑습니다^^')"

sql = "select writer, title, contents from board"

cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()

conn.close()
