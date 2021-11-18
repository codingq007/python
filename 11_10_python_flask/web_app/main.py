from web_app import *

@app.route("/")
def home():
    return render_template("home.html")