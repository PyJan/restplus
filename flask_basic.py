from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>main page</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h2>hello {}</h2>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
