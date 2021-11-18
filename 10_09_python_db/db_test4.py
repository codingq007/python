import sqlite3

conn = sqlite3.connect('../resource/students.db', isolation_level=None)

# cursor 바인딩
cur = conn.cursor()

cur.execute("create table if not exists students(stu_id integer primary key, name text, tel text, addr text)")

cur.execute("create table if not exists score(stu_id integer primary key, os integer, comVision integer, db integer)")


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

def set_student():
    stu_id = input('학번 : ')
    name = input('이름 : ')
    tel = input('전화번호 : ')
    addr = input('주소 : ')
    student = Student(stu_id, name, tel, addr)
    return student


def insert_student(student):
    cur.execute("insert into students values(?,?,?,?)",(student.stu_id, student.name, student.tel, student.addr))
    print('학생 정보 입력 완료')

def print_student():
    cur.execute("select * from students")
    student_list = cur.fetchall()
    return student_list

def set_score():
    stu_id = int(input('학번 : '))
    cur.execute("select * from students where stu_id = ?", (stu_id,))
    res_stu = cur.fetchone()
    # print(res_stu)
    if res_stu != None:
        cur.execute("select * from score where stu_id = ?", (stu_id,))
        res_score = cur.fetchone()

        if res_score != None:
            print('이미 입력되었습니다!!!')
        else:
            print('성적을 입력하세요')
            os = input('운영체제 : ')
            comVision = int(input('컴퓨터비전 : '))
            db = int(input('데이터베이스 : '))

            score = Score(stu_id, os, comVision, db)
            return score
    else:
        print('학생이 존재하지 않습니다!!!')    


def insert_score(score):
    cur.execute("insert into score values(?,?,?,?)", (score.stu_id, score.os, score.comVision, score.db))
    print("성적 입력 완료!!")

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
        3. 학생 성적 입력
        4. 학생 성적 출력
        종료 : x
        -----------------------------
    ''')

    menu = input('메뉴 선택 : ')
    if menu == 'x':
        return menu
    return int(menu)

def run():
    while 1:
        menu = menu_display()
        if menu == 1:
            student = set_student()
            insert_student(student) 
        elif menu == 2:            
            # student_list = print_student()
            for student in print_student():
                for col in student:
                    print(col, end='\t')
                print()
            print()

            print('전체 학생 수 : ', student_cnt(),'명')
        elif menu == 3:
            # stu_id = int(input('학번 : '))
            score = set_score()
            if score !=None:
                insert_score(score)
            # score_input(stu_id)
            # score_input()
        elif menu == 4:
            print('''
            -------------------------------------------------------------------
               학번\t이름\t운영체제 컴퓨터비전 데이터베이스 총점\t평균
            -------------------------------------------------------------------
            ''') 
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