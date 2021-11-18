import sqlite3
import common.consts as const

def db_conn():
    conn = sqlite3.connect(const.DB_PATH, isolation_level=None)
    conn.execute("PRAGMA foreign_keys = 1") # 외래키 Lock(on) 해제, sqlite는 기본이 Lock(off)

    # cursor 바인딩
    cur = conn.cursor()

    cur.execute("create table if not exists students(\
        stu_id integer primary key, \
        name text, tel text, addr text)")

    # on update cascade : 기본키 수정시 외래키가 자동 수정됨
    cur.execute("create table if not exists score(\
        stu_id integer,\
        os integer, comVision integer, db integer,\
        foreign key(stu_id) references students(stu_id) on update cascade)")

    return cur