from flask import Flask

app = Flask(__name__)

topics = [
    {'id':1, 'title': 'html', 'body': 'html is ...'},
    {'id':2, 'title': 'css', 'body': 'css is ...'},
    {'id':3, 'title': 'js', 'body': 'js is ...'},
]

def template(contents, content):
    return f'''<!doctype html>
        <html>
            <body>
                <h1><a href="/">Hello</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
            </body>
        </html>
    
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<int:id>/') # 읽기, id 정수로 지정
def read(id):
    # print(type(id)) 
    # 변환전에는 str
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    # print(title,body)
    return template(getContents(), f'<h2>{title}</h2>{body}') 


app.run(debug=True) 

