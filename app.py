from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#@app.route("/Bye")
#def bye():
  #  return "Bye World!"

#@app.route('/user')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
    