import time

# 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여
# 함수의 기능을 확장시키는 개념

# def outer_fun(param):
#     def inner_fun():
#         return f'내부 함수인데 {param} 매개변수를 받았음.'
#     return inner_fun


# cc = outer_fun('Hello World!!')

# print(cc())

# def test():
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)
#     end_time = time.time() - start_time
#     print(f"함수 동작 시간 : {end_time}")


# test()    

def chk_time(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"함수 {func.__name__} 동작시간 : {end_time - start_time}")
        return result
    return inner_func


# chk_time함수와 test1을 합치기
@chk_time
def test1():
    for i in range(5):
        time.sleep(0.1)

# chk_time함수와 test2을 합치기
@chk_time
def test2():
    for i in range(8):
        time.sleep(0.1)

test1()
test2()









