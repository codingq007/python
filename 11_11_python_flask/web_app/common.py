from web_app import *

def login_required(f):
    @wraps(f)
    def check_function(*args, **kwargs):
        if session.get("id") is None or session.get("id") == "":
            # request.url은 현재 url을 의미한다.
            return redirect(url_for("member.member_login", next_url=request.url))
        return f(*args, **kwargs)
    return check_function

# 서버에 파일을 첨부할 때 첨부되는 파일명은 위험 요소가 많기 때문에 항상 신경을 써야한다.
# 파일명을 악의적으로 이용해서 서버의 권한을 탈취하는 경우가 발생할 수 있기 때문에
# 그런한 위험요소를 제거해야한다. 플라스크에서는 secure_filename()을 제공하는데..한글 체크는
# 하지 않는다.. 따라서, 한글까지 체크하는 함수를 만들어서 처리

def check_filename(filename):
    reg = re.compile("[^A-Za-z0-9_.가-힝-]")

    for sp in os.path.sep, os.path.altsep:
        if sp:
            filename = filename.replace(sp, ' ')

            filename = str(reg.sub('','_'.join(filename.split()))).strip("._")
    return filename

# check_filename("../../../../home/username/.bashrc") --> homeusername.bashrc

# 파일 확장자를 체크하는 함수
# 예> aaa.bbb.cc.jpg 파일명에서 마지막 확장자 jpg만 가져와서 ALLOWED_EXTENSIONS에 있는지
# rsplit(".", 1) 오른쪽부터 .을 기준으로 split을 하는데 1은 마지막 하나만 split을 한다는 의미
# 그러면 ["aaa.bbb.cc", "jpg"] 리스트로 반환 [1]은 두번째 인자 jpg
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

def rand_generator(length = 8):
    # 모든 대소문자, 숫자가 char안에 포함된다.
    char = ascii_uppercase + ascii_lowercase + digits
    return "".join(random.sample(char, length))