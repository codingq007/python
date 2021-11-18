from functools import wraps

# def test():
#     '''테스트 함수'''
#     return 'Hello'

# print(test.__name__)    
# print(test.__doc__)    

def temp_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"데코레이터 {func(*args, **kwargs)}"
    return wrapper

# 데코레이터를 사용할 경우에
# 원래 함수가 갖고 있던 속성 name, doc,... 등이 사라지는 문제가 발생
# 이런 문제점을 방지하기 위해서 functools모듈의 @wrap를 이용해서 해결할 수 있다.
@temp_decorator
def test():
    '''테스트용 함수'''    
    return 'Hello'

print(test.__name__)    
print(test.__doc__)    
