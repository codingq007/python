from flask import Flask
from flask import request, render_template,redirect,url_for, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import time
import math


app = Flask(__name__)

# webtest는 데이터베이스명
app.config["MONGO_URI"] = "mongodb://localhost:27017/webtest"
mongo = PyMongo(app)

@app.template_filter('datetime_format')
def datetime_format(value):
    if value is None:
        return ""

    # 클라이언트의 현재 시스템의 local 타임
    # 클라이언트의 local 타임을 datetime형식으로 만들어서 표현
    # 게시글을 보는 사람이 있는 지역의 시간(현재 컴퓨터의 시간)
    now_timestamp = time.time()
    print("현재 로컬 타임 :", now_timestamp)

    # datetime 객체에 fromtimestamp, utcfromtimestamp 함수가 있다.

    # 클라이언트의 시간을 기준으로 datetime 객체를 만듦
    print(datetime.fromtimestamp(now_timestamp))

    # utcfromstamp는 UTC datetime 을 반환
    # db에 저장된 UTC format과 같은 형태로 반환됨
    print(datetime.utcfromtimestamp(now_timestamp))

    # 시간차 
    offset_time = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    print("offset_time : ", offset_time)

    # db에 저장된 UTC 타임을 다시 현재의 로컬타임으로 변환해줌
    value = datetime.fromtimestamp((int(value) / 1000)) + offset_time

    # strftime() : format을 변경하는 함수
    return value.strftime('%Y-%m-%d %H:%M:%S')

######################## list ########################
@app.route("/list")
def lists():
    # 페이지 값(값이 없는 경우에는 기본값을 1로하고, 그 자료형은 int형)
    page = request.args.get("page", default=1, type=int)

    # 한페이지당 몇개의 게시물을 출력할지를 지정(보통 고정해서 사용하는 경우도 많음)
    limit = request.args.get("limit", 10, type=int)

    board = mongo.db.board
    # 현재 페이지가 2페이지이면 (2-1)*10은 건너띄고, 10개만 표시 limit(10)
    docs = board.find({}).skip((page-1) * limit).limit(limit)

    ## 전체 게시물의 개수
    total_cnt = board.find({}).count()

    ## 마지막 페이지 수
    last_page_num = math.ceil(total_cnt/limit)

    # 한블럭에 보여줄 페이지 수
    block_size = 5

    # 현재 페이지의 블럭 위치 계산하기(0, 1, 2, ...)
    block_num = int((page - 1) /block_size)

    # 블럭의 시작값 : 첫번째 블럭 시작값 1, 두번째 블럭 시작값 6
    block_start = int((block_size * block_num) + 1)

    # 블럭의 마지막값 : 첫번째 블럭의 마지막 값 5, 두번째 ~ : 10
    # 첫번째 블럭의 마지막 값: 1 + 4, 두번째 블럭의 마지막 값 : 6 + 4
    block_last = block_start + (block_size - 1)

    # return render_template("list.html", docs = docs)

    return render_template("list.html", docs = docs,
                                        page = page,
                                        limit = limit,
                                        block_start = block_start,
                                        block_last = block_last,
                                        last_page_num = last_page_num)


######################## view ########################
# clean url, fancy url 표기법(사용편의성, 보안적인 측면고려)
@app.route('/view/<idx>')
def board_view(idx):
# @app.route('/view')
# def board_view():
    # idx = request.args.get("idx")
    if idx is not None:
        board = mongo.db.board

        # 게시물은 하나 따라서, find_one, idx를 ObjectId로 변환
        data = board.find_one({"_id":ObjectId(idx)})

        if data is not None:
            result = {
                "id": data.get("_id"),
                "name": data.get("name"),
                "title": data.get("title"),
                "contents":data.get("contents"),
                "regdate" : data.get("regdate"),
                "hit" : data.get("hit")
            }

            return render_template("view.html", result = result)
    return abort(404) # 오류 출력


######################## write ########################
# methods 지정하지 않으면 GET방식
@app.route('/write', methods=["GET", "POST"])
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        print(name, title, contents)

        # utc는 국제 표준시(GMT(Greenwich Mean Time)) : UTC, GMT 혼용하여 사용한다.
        # UTC, GMT는 시간차가 거의 없음.

        # 데이터베이스에 시간을 저장할 때는 가장 가공하기 쉬운
        # 형태로 저장을 해놓아야 한다.  
        # 재가공하기 쉬운 형태가 바로 timestamp이다.

        # utc time은 1000분의 1초로 표현        
        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        # 컬렉션 생성
        board = mongo.db.board

        post_data = {
            "name": name,
            "title": title,
            "contents":contents,
            "regdate" : current_utc_time,
            "hit": 0
        }

        doc = board.insert_one(post_data)
        # return str(doc.inserted_id)
        return redirect(url_for("board_view", idx=doc.inserted_id))
    else:
        return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)

