from flask import Flask
import random

app = Flask(__name__)

# 어떤 요청을 어떤 함수가 응답할 것인가를 연결시키는 작업 -> 라우팅

@app.route('/')
def index():
    return 'Welcome' 

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/') # Variable Rules
def read(id):
    return 'Read '+id

app.run(debug=True) 

