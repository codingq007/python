from functools import wraps

def login_required(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get('is_login'):
            return '서비스를 제공받기 위해서는 로그인이 필요합니다!!'
        return func(*args, **kwargs)
    return wrapper

@login_required
def login_test(is_login=False):
    print("당신은 로그인 되었습니다.")

print("1 : ", login_test()) 

@login_required
def login_test(*args, **kwargs):
    print("당신은 로그인 되었습니다!!")

login_test(is_login = True)    


