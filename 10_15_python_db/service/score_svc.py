from db.db_connection import db_conn
from common.input_chk import input_id, chk_id
from model.score import Score

cur = db_conn()
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
