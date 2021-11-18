from flask import Flask
from flask import request, render_template
from flask_pymongo import PyMongo
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/webtest"
mongo = PyMongo(app)

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
        return str(doc.inserted_id)
    else:
        return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)

