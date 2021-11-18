from flask import Flask, session
from flask import request, render_template,redirect,url_for, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from functools import wraps
import time
import math


app = Flask(__name__)
# webtest는 데이터베이스명
app.config["MONGO_URI"] = "mongodb://localhost:27017/webtest"

# flash를 사용하게 되면 SECRET_KEY를 사용해야 한다.
app.config["SECRET_KEY"] = "test1234" # 노출되면 안되틑 암호화된키
mongo = PyMongo(app)

# 세션의 유지시간은 환경변수에 설정한다.
# 설정 시에는 timedelta()함수를 이용해서 설정한다. 
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 30)
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds = 5)

from .common import login_required
from .filter import datetime_format

# web_app 패키지에 각 모듈을 귀속시킨다.
from . import board
from . import member
