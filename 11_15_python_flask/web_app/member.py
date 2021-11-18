from web_app import *


bp = Blueprint("member", __name__, url_prefix="/member")

######################## join ########################
@bp.route("/join", methods=["GET", "POST"])
def member_join():
    if request.method == "POST":
        name = request.form.get("name", type=str)
        email = request.form.get("email", type=str)
        pw1 = request.form.get("pw1", type=str)
        pw2 = request.form.get("pw2", type=str)

        if name == "" or email =="" or pw1 == "" or pw2 == "":
            '''
            flask는 플래싱 시스템을 가지고 user에게 피드백을 주는 방법을 제공
            플래싱 시스템은 기본적으로 요청의 끝에 메시지를 기록하고 그 다음 요청에서만
            그 메시지를 접근할 수 있게 한다.

            보통 플래싱을 처리하는 레이아웃 템플릿과 결합되어 사용

            메시지를 html에 보내는 기능의 함수, 일회성 메시지
            '''
            flash("유효하지 않은 값이 있습니다!!")
            return render_template("member/join.html")
        
        if pw1 != pw2 :
            flash("비밀번호가 일치하지 않습니다!!")
            return render_template("member/join.html")

        # members collection 생성
        members = mongo.db.members

        # 중복 회원이 있는지 체크하기
        cnt = members.find({"email":email}).count()
        if cnt > 0:
            flash("중복된 이메일이 있습니다!! 다시 확인하세요...")
            return render_template("member/join.html")

        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        post_data = {
            "name":name,
            "email":email,
            "pw":hash_pw(pw1),
            "join_date":current_utc_time,
            "login_time":"",
            "login_count": 0,
        } 

        members.insert_one(post_data)
        return redirect(url_for("member.member_login"))
    else:
        return render_template("member/join.html")

######################## login ########################
@bp.route("/login", methods=["GET", "POST"])
def member_login():
    if request.method == "POST":
        email = request.form.get("email")
        pw = request.form.get("pw")

        # login_required를 통해 로그인을 강요받은 경우
        # GET /login --> login.html(로그인 버튼 submit) --> POST /login
        # 위 순서대로 로그인 처리됨.

        # next_url이 있으면 받고, 없으면 None으로 처리
        next_url = request.form.get("next_url")

        members = mongo.db.members
        doc = members.find_one({"email": email})

        if doc is None:
            flash("회원 정보가 없습니다.")
            return redirect(url_for("member.member_login"))
        else:
            # 파이썬에서 session은 딕셔너리 형태로 저장된다.            
            # if doc.get("pw") == pw:
            if check_pw(doc.get("pw"), pw):
                current_utc_time = round(datetime.utcnow().timestamp()*1000)
                members.update_one({"email":email}, {
                    "$set": {"login_time":current_utc_time},
                    "$inc" : {"login_count": 1}
                })

                session["email"] = email
                session["name"] = doc.get("name")
                session["id"] = str(doc.get("_id"))

                # 세션은 서버에 저장된다. 따라서, 서버 자원의 효율적인 관리를 위해서
                # 일정시간안에 접속을 하면 세션이 유지가 되고,
                # 일정시간동안 클라이언트가 접속하지 않으면 초기화된다.
                # 모든 서버에서는 세션의 기본 유지 시간이 설정되어 있다.

                # 여기서는 임의로 세션의 유지시간을 할당을 하기위해서
                # session의 permanent 값을 True 로 설정한다.
                session.permanent = True

                
                # next_url이 있으면 접속하려 했던 페이지로 이동, 사용자의 편의성을 위해서
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect(url_for("board.lists"))
            else:
                flash("비밀번호가 일치하지 않습니다.")
                return redirect(url_for("member.member_login"))

        return ""
    else:
        next_url = request.args.get("next_url", type=str)
        if next_url is not None:
            return render_template("member/login.html", next_url=next_url)
        else:
            return render_template("member/login.html")


@bp.route("/logout")
def logout():
    # 세션 초기화
    session.clear()    
    return redirect(url_for("board.lists"))