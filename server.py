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
                <ul>
                    <li><a href="/create/">create</a></li>
                </ul>    
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
    content = '''
        <form action="/create/" method="POST"> 
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>  
            <p><input type="submit" value="create"></p>
        </form>
    '''
    # POST 방식 - 데이터가 url 을 통해 전송되지 않음. 데이터를 사용자가 변경할 때 사용
    return template(getContents(),content)

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

