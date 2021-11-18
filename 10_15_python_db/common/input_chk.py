from db.db_connection import db_conn

cur = db_conn()
################################ 학번 입력 () #############################
def input_id():
    while True:
        try:
            return int(input('학번 : '))
        except ValueError:
            print('다시 입력하세요')    

################################ 학번 체크 () #############################
def chk_id(stu_id, n=2):  
    if n==2:
        cur.execute("select * from students where stu_id = ?", (stu_id,))
        res_stu = cur.fetchone()

        cur.execute("select * from score where stu_id = ?", (stu_id,))
        res_score = cur.fetchone()

        return res_stu, res_score

    if n ==1:
        cur.execute("select * from students where stu_id = ?", (stu_id,))
        res_stu = cur.fetchone()

        return res_stu

    if n ==0:
        cur.execute("select * from score where stu_id = ?", (stu_id,))
        res_score = cur.fetchone()

        return res_score
