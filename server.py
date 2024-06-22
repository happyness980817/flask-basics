from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title': 'html', 'body': 'html is ...'},
    {'id':2, 'title': 'css', 'body': 'css is ...'},
    {'id':3, 'title': 'js', 'body': 'js is ...'},
] # 데이터베이스에서 데이터 불러오기


@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>
        <html>
            <body>
                <h1><a href="/">Hello</a></h1>
                <ol>
                    {liTags}
                </ol>
            </body>
        </html>
    
    '''

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/') 
def read(id):
    return 'Read '+id

app.run(debug=True) 

