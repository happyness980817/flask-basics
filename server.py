from flask import Flask, request, redirect

app = Flask(__name__)

nextId = 4
topics = [
    {'id':1, 'title': 'html', 'body': 'html is ...'},
    {'id':2, 'title': 'css', 'body': 'css is ...'},
    {'id':3, 'title': 'js', 'body': 'js is ...'},
] # 데이터베이스에서 데이터 불러오기

def template(contents, content, id=None):
    contextUI = ''
    if id != None: # update, delete 는 id 가 있을때만 사용
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>
        '''
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
                    {contextUI} 
                </ul>    
            </body>
        </html>
    
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/') # We then use the route() decorator to tell Flask what URL should trigger our function.
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

# The function returns the message we want to display in the user’s browser. 
# The default content type is HTML, so HTML in the string
# will be rendered by the browser.

@app.route('/read/<int:id>/') # Variable Rules - id 정수로 지정
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
    return template(getContents(), f'<h2>{title}</h2>{body}', id) 

@app.route('/create/', methods=['GET','POST']) # get 이 아닌 method 허용할 시 methods 지정
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST"> 
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>  
                <p><input type="submit" value="create"></p>
            </form>
        '''
    elif request.method == 'POST':
        global nextId # 외부에서 생성된 전역변수 초기값 참조
        title = request.form['title'] # To access form data 
        # (data transmitted in a POST or PUT request) 
        # you can use the form attribute. 
        body = request.form['body']
        newTopic = {'id':nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/' + str(nextId) + '/'
        nextId += 1
        return redirect(url) # redirection: redirects a user to another endpoint

    # POST 방식(method) - 데이터가 url 을 통해 전송되지 않음. 데이터를 사용자가 변경할 때 사용
    return template(getContents(),content)

@app.route('/update/<int:id>/', methods=['GET','POST']) 
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST"> 
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>  
                <p><input type="submit" value="update"></p>
            </form>
        ''' # 요기는 기존의 데이터 가져오는 부분 (수정할것들)(read)
    elif request.method == 'POST':
        title = request.form['title'] 
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/' + str(id) + '/'
        return redirect(url) 

    return template(getContents(),content)

@app.route('/delete/<int:id>/', methods=['POST']) 
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')

app.run(host='0.0.0.0') 

