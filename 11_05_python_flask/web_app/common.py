from web_app import wraps, session, redirect, url_for,request

def login_required(f):
    @wraps(f)
    def check_function(*args, **kwargs):
        if session.get("id") is None or session.get("id") == "":
            # request.url은 현재 url을 의미한다.
            return redirect(url_for("member_login", next_url=request.url))
        return f(*args, **kwargs)
    return check_function