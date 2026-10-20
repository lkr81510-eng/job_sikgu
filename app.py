from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/search")
def search():
    return "hi 안녕하세요 반갑습니다."

if __name__ == '__main__':
     app.run(debug=True)