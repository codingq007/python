# 템플릿 표현식 사용하기

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template('temp.html', my_string="템플릿 테스트", my_list=[11,22,33,44,55,66,77])


if __name__ == '__main__':
    app.run(debug=True, port=9000)        
