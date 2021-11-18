import sqlite3
# from sqlite3.dbapi2 import enable_callback_tracebacks

conn = sqlite3.connect('../resource/students.db', isolation_level=None)
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

# cur.execute("create table if not exists score(\
#     stu_id integer primary key,\
#     os integer, comVision integer, db integer)")


# 학생 정보 클래스
class Student:
    def __init__(self, stu_id, name, tel, addr):
        self.stu_id = stu_id
        self.name = name
        self.tel = tel
        self.addr = addr

# 성적 클래스
class Score:
    def __init__(self, stu_id, os, comVision, db):
        self.stu_id = stu_id
        self.os = os
        self.comVision = comVision
        self.db = db
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



################################ 학생 객체 생성/ DB 입력 () #############################
def insert_student():
    while True:
        stu_id = input_id()
        res1 = chk_id(stu_id, 1)

        # 등록된 학생의 학번이 있는지 체크(중복 여부 체크)
        # 학번은 primary key: unique + not null
        if res1 != None:
            print('존재하는 학번입니다... 다시 입력하세요!!')
        else:
            name = input('이름 : ')
            tel = input('전화번호 : ')
            addr = input('주소 : ')
            student = Student(stu_id, name, tel, addr)

            cur.execute("insert into students values(?,?,?,?)",(student.stu_id, student.name, student.tel, student.addr))
            print('학생 정보 입력 완료')
            break

    # return student

################################ 학생 정보 DB 입력 () #############################
# def insert_student(student):
#     cur.execute("insert into students values(?,?,?,?)",(student.stu_id, student.name, student.tel, student.addr))
#     print('학생 정보 입력 완료')

################################ 학생 조회 () #############################
def print_student():

    print('--------------------------------------------------------------------')
    print(f'{"학번":^6} {"이름":^8} {"전화번호":^10} {"주소":^10} {"성적입력":^8}')
    print('--------------------------------------------------------------------')

    cur.execute("select * from students")
    students = cur.fetchall()

    # for student in print_student():
    #     for col in student:
    #         print(col, end='\t')    
    #     print()
    
    for student in students:
        print(f'{student[0]:^7}', end=' ') # stu_id
        print(f'{student[1]:^8}', end=' ') # name
        print(f'{student[2]:^13}', end=' ') # tel
        print(f'{student[3]:^15}', end=' ') # addr

        # 성적 테이블에 해당 학생 id가 있는지 체크
        res = chk_id(student[0], 0)

        # 각 학생의 학번이 성적 테이블에 있으면 입력, 없으면 미입력을 출력
        if res != None:
            print(f'{"입력":^8}')
        else:
            print(f'{"미입력":^8}')
    print('--------------------------------------------------------------------')

    print('전체 학생 수 : ', student_cnt(),'명')


    # return student_list

################################ 학생 정보 DB 수정 () #############################
def update_student():
    stu_id = input_id()
    res1 = chk_id(stu_id, 1)    

    # 학번이 있으면
    if res1 !=None: 
        while True:
            print('----------------------')
            print('1. 이름 수정 ')
            print('2. 전화번호 수정 ')
            print('3. 주소 수정 ')
            print('4. 아이디 수정 ')
            print('5. 수정 완료 ')
            print('----------------------')

            try:
                update_menu = int(input('> 메뉴 선택 : '))
            except ValueError:
                print('1 ~ 4 숫자만 입력 가능')
                continue

            if update_menu == 1:
                update_name = input('수정할 이름 입력 : ')
                cur.execute("update students set name=? where stu_id=?",(update_name, stu_id))
            elif update_menu == 2:
                update_tel = input('수정할 전화번호 입력 : ')
                cur.execute("update students set tel=? where stu_id=?",(update_tel, stu_id))
            elif update_menu == 3:
                update_addr = input('수정할 주소 입력 : ')
                cur.execute("update students set addr=? where stu_id=?",(update_addr, stu_id))
            elif update_menu == 4: 
                update_id = input('수정할 id 입력 : ')
                cur.execute("update students set stu_id=? where stu_id=?",(update_id, stu_id)) 
                # cur.execute("update score set stu_id=? where stu_id=?",(update_id, stu_id)) 

            elif update_menu == 5:
                return
    else:
        print('학번이 존재하지 않습니다!!!')

################################ 학생 성적 DB 수정 () #############################
def update_score():
    stu_id = input_id()
    res1, res2 = chk_id(stu_id)
    if res1 !=None:
        if res2 !=None:
            while True:
                print('----------------------')
                print('1. 운영체제 점수 수정 ')
                print('2. 컴퓨터비전 점수 수정 ')
                print('3. 데이터베이스 점수 수정 ')
                print('4. 전과목 점수 수정 ')
                print('5. 수정 완료 ')
                print('----------------------')

                try:
                    update_menu = int(input('> 메뉴 선택 : '))
                except ValueError:
                    print('1 ~ 5 숫자만 선택 가능')
                    continue

                if update_menu == 1:
                    update_os = input('운영체제 점수 입력 : ')
                    cur.execute("update score set os=? where stu_id=?",(update_os, stu_id))
                elif update_menu == 2:
                    update_cv = input('컴퓨터비전 점수 입력 : ')
                    cur.execute("update score set comVision=? where stu_id=?",(update_cv, stu_id))
                elif update_menu == 3:
                    update_db = input('DB 점수 입력 : ')
                    cur.execute("update score set db=? where stu_id=?",(update_db, stu_id))
                elif update_menu == 4:
                    print('운영체제, 컴퓨터비전, 데이터베이스 순으로 점수를 입력하세요!!')
                    os, cv, db = input("입력 예: 90,80,70 > ").split(',')
                    cur.execute('update score set os=?, comVision=?, db=? where stu_id = ?', (int(os), int(cv), int(db), stu_id))
                elif update_menu == 5:
                    return
        else:
            print('성적을 먼저 입력하세요!!')

    else:
        print('학번이 존재하지 않습니다!!!')


################################ 학생 정보 DB 삭제() #############################
def delete_student():
    stu_id = input_id()
    res1, res2 = chk_id(stu_id)

    if res1 !=None:
        # 성적이 있는 학생 삭제
        if res2 !=None:
            cur.execute("delete from students where stu_id = ?", (stu_id,))
            cur.execute("delete from score where stu_id = ?", (stu_id,))
            print(f"{stu_id}번 학생이 삭제되었습니다!!")
        # 성적이 없는 학생 삭제
        else: 
            cur.execute("delete from students where stu_id = ?", (stu_id,))
            print(f'{stu_id}번 학생이 삭제되었습니다!!')
    else:
        print('학번이 존재하지 않습니다!!!')        


################################ 성적 객체 생성/ DB 입력 () #############################
def insert_score():
    stu_id = input_id()
    res1, res2 = chk_id(stu_id)

    if res1 != None:
        if res2 != None:
            print('이미 입력되었습니다!!!')
        else:
            print('성적을 입력하세요')
            os = input('운영체제 : ')
            comVision = int(input('컴퓨터비전 : '))
            db = int(input('데이터베이스 : '))

            score = Score(stu_id, os, comVision, db)
            cur.execute("insert into score values(?,?,?,?)", (score.stu_id, score.os, score.comVision, score.db))
            print("성적 입력 완료!!")
            # return score
    else:
        print('학생이 존재하지 않습니다!!!')    

################################ 성적 DB 입력 () #############################
# def insert_score(score):
#     cur.execute("insert into score values(?,?,?,?)", (score.stu_id, score.os, score.comVision, score.db))
#     print("성적 입력 완료!!")

def student_cnt():
    cur.execute("select count(*) from students")
    cnt = cur.fetchone()
    return cnt[0]

def menu_display():
    print('''
        ------------------------------
               학사 관리 시스템
        -----------------------------
        1. 학생 정보 입력
        2. 학생 정보 출력
        3. 학생 정보 수정
        4. 학생 정보 삭제
        5. 학생 성적 입력
        6. 학생 성적 출력
        7. 학생 성적 수정
        x. 종료
        -----------------------------
    ''')

    menu = input('메뉴 선택 : ')
    if menu == 'x':
        return menu
    return int(menu)
################################ 성적 조회 () #############################
def print_score():
    print('-------------------------------------------------------------------')
    print('  학번\t이름\t운영체제 컴퓨터비전 데이터베이스 총점\t평균')
    print('-------------------------------------------------------------------')

    # join
    cur.execute("select stu.stu_id, stu.name, sc.os, sc.comVision, sc.db\
        from students stu, score sc \
        where sc.stu_id = stu.stu_id")

    for student in cur.fetchall():
        print(student[0], end='\t')    
        print(student[1], end='\t')    
        print(student[2], end='\t\t')    
        print(student[3], end='\t')    
        print(student[4], end='\t')  

        score_sum = student[2] + student[3] + student[4]
        print(score_sum, end='\t') 

        score_avg = format(score_sum/3, '.2f')
        print(score_avg)
    print('----------------------------------------------------------------')


def run():
    while 1:
        menu = menu_display()
        if menu == 1:
            # student = set_student()
            insert_student() 
        elif menu == 2:            
            # student_list = print_student()
            print_student()
        elif menu == 3:
            update_student()

        elif menu == 4:
            delete_student()
        elif menu == 5:
            insert_score()
            # score = set_score()
            # if score !=None:
            #     insert_score(score)
        elif menu == 6:
            print_score()
 
        elif menu == 7:
            update_score()
        elif menu == 'x':
            break

if __name__ == '__main__':
    run()

## 과제물
    # print('1. 학생 정보 입력')
    # print('2. 학생 정보 출력')
    # print('3. 학생 정보 수정')
    # print('4. 학생 정보 삭제')
    # print('5. 학생 성적 입력')
    # print('6. 학생 성적 출력')
    # print('7. 학생 성적 수정')
    # print('X. 프로그램 종료')  