from service.student_svc import insert_student, print_student, update_student, delete_student
from service.score_svc import insert_score, update_score, print_score

# import common.consts as const

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


def run():
    while 1:
        menu = menu_display()
        if menu == 1:
        # if menu == const.INPUT_STUDENT:
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
