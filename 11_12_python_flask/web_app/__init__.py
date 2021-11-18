from flask import Flask, session, Blueprint,send_from_directory
from flask import request, render_template,redirect,url_for, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from functools import wraps
import time, random
import math, os
from string import ascii_lowercase, ascii_uppercase, digits
import re # 정규식 모듈
from flask_wtf.csrf import CSRFProtect

# CSRF(Cross site Request Forgery : 크로스 사이트 요청변조 ) 공격 

# 대부분의 게시판에서 자바스크립트 공격을 막아 놓는다. 하지만, 이미지 포스팅은 막지 않는 경우가 많다.
# 이미지는 get방식 링크
# 서버의 값을 바꾸는 경우는 get방식을 사용하지 않고, post방식으로 해야한다. 
# post방식도 안전하지 않다.. 따라서, 서버에서 토큰값을 받아와 매번 접속할 때 마다 인증을 해야 한다.

# CSRF공격은 보통 form 데이터가 전송되거나, 받는 경우에 많이 발생한다. 
# 이러한 공격을 방어하기 위해서 대부분의 프레임워크에서 지원을 하고 있다.

# 플라스크에서는 pip install flask-wtf


app = Flask(__name__)
csrf = CSRFProtect(app) # csrf 공격 방어가 되도록 동작하게 된다.


# webtest는 데이터베이스명
app.config["MONGO_URI"] = "mongodb://localhost:27017/webtest"

# flash를 사용하게 되면 SECRET_KEY를 사용해야 한다.
app.config["SECRET_KEY"] = "test1234" # 노출되면 안되틑 암호화된키
mongo = PyMongo(app)

BOARD_IMAGE_PATH = "C:\\flask\\images"
BOARD_ATTACH_FILE_PATH = "C:\\flask\\uploads"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg'])

app.config["BOARD_IMAGE_PATH"] = BOARD_IMAGE_PATH
app.config["BOARD_ATTACH_FILE_PATH"] = BOARD_ATTACH_FILE_PATH
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

if not os.path.exists(app.config["BOARD_IMAGE_PATH"]):
    os.mkdir(app.config["BOARD_IMAGE_PATH"])

if not os.path.exists(app.config["BOARD_ATTACH_FILE_PATH"]):
    os.mkdir(app.config["BOARD_ATTACH_FILE_PATH"])

# 세션의 유지시간은 환경변수에 설정한다.
# 설정 시에는 timedelta()함수를 이용해서 설정한다. 
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 30)
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds = 5)

from .common import login_required, allowed_file, rand_generator, check_filename, hash_pw, check_pw
from .filter import datetime_format

# web_app 패키지에 각 모듈을 귀속시킨다.
from . import board
from . import member
from . import main

app.register_blueprint(board.bp)
app.register_blueprint(member.bp)
