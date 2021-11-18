# jinja2 템플릿 엔진
# flask 설치시 같이 설치
# 플라스크의 템플릿 파일들은 기본적으로 templates 폴더에 저장

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!!</h1>'

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name = username)

if __name__ == '__main__':
    app.run(debug=True, port=9000)        
