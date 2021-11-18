from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello Wrold!!</h1>'

# username은 string타입의 변수를 의미
@app.route('/user/<username>')
def show_user(username):
    return 'User : %s' % username

# int 타입의 post_id 파라미터
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post : %d' %post_id  

@app.route('/circle/<float:pi>')
def show_pi(pi):
    return 'PI %f' % pi

@app.route('/test/path/<path:subpath>')    
def path(subpath):
    return subpath

@app.route('/test/redirect/<path:subpath>')
def redirect_url(subpath):
    return redirect(subpath)

@app.route('/test/urlfor/<path:subpath>')    
def urlfor(subpath):
    return redirect(url_for('path', subpath=subpath))


if __name__ == "__main__":
    app.run(debug=True, port=9000)