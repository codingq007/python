# pip install flask

from flask import Flask

# flask 인스턴스 생성
# 인스턴스 생성시에 현재 모듈을 인자로 넣어준다.
app = Flask(__name__)

# 주소를 선언
@app.route("/")
# @app.route("/hello")
def index():
    return '<h1>Hello Flask!!</h1>'


if __name__ == "__main__":
    app.run(debug=True, port=9000)
