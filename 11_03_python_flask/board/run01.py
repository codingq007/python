from flask import Flask
from flask import request, render_template

app = Flask(__name__)

# methods 지정하지 않으면 GET방식
@app.route('/write', methods=["GET", "POST"])
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        print(name, title, contents)
        return ""
    else:
        return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)

