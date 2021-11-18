from flask import Flask
from flask import request, render_template,redirect,url_for, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import time


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

