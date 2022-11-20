from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>main page</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h2>hello {name}</h2>'

if __name__ == '__main__':
    app.run(debug=True)
