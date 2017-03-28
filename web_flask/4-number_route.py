from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    return "C {}".format(text)

@app.route('/python/', defaults={'text': "is_cool"})
@app.route('/python/<text>')
def python(text):
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
