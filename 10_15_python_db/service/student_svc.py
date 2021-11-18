from common.input_chk import input_id, chk_id
from db.db_connection import db_conn
from model.student import Student

cur = db_conn()

################################ 학생 수 조회 () #############################
def student_cnt():
    cur.execute("select count(*) from students")
    cnt = cur.fetchone()
    return cnt[0]

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
