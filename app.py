from flask import Flask, render_template
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/apply")
def apply():
    return render_template("apply.html")

@app.route("/list")
def list():
    return render_template("list.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')