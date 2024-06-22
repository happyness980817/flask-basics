from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>' +str(random.random())+'</strong>' # 브라우저에 html 전달

app.run(debug=True) #서버 닫지 않아도 새로고침하면 변경사항 반영, 실제 서비스시에는 X

