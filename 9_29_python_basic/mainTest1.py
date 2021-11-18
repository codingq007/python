
a = 100
def test1():
    print('테스트 함수1')

def test2():
    print('테스트 함수2')    

# 단위 테스트
if __name__ == '__main__':
   test1()
   test2()
else:
    print('현재 이파일이 import되었을 때의 __name__ :', __name__)
   
