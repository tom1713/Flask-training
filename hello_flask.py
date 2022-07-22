from tokenize import Name
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import json

app = Flask(
    __name__,
    static_folder = "public",
    static_url_path = "/"
)
app.secret_key="123"

@app.route("/")
def index():
    return render_template("index.html")
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    # lang = request.headers.get("accept-language")
    # if lang.startswith("en"):
    #     return redirect("/en/")
    # else:
    #     return redirect("/zh_TW/")

@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/show")
def show():
    name = request.args.get("n", "")
    session["userName"] = name
    return "歡迎光臨 " + name

@app.route("/talk")
def talk():
    name = session["userName"]
    return name + " 很高興見到你"

@app.route("/en/")
def index_english():
    return json.dumps({
        "status" : "OK",
        "text" : "Hello flask"
    })

@app.route("/zh_TW/")
def index_chinese_TW():
    return json.dumps({
        "status" : "好",
        "text" : "你好 歡迎光臨"
    },ensure_ascii = False)

@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<name>")
def handleuser(name):
    if name == "kai" :
        return "你好 " + name
    else :
        return "Hello " + name

@app.route("/getSum", methods=["POST"])
def getSum():
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    # maxNumber = request.args.get("max", 100)
    maxNumber = request.form["max"]
    maxNumber = int(maxNumber)
    result = 0
    for n in range(minNumber, maxNumber + 1):
        result += n
    return render_template("result.html", data = result)

app.run(port=2000)