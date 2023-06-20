# Put your app in here.
from flask import Flask, request
from operations import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = multiply(a, b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = divide(a, b)
    return str(result)

if __name__ == '__main__':
    app.run()