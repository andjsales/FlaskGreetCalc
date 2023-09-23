# Put your app in here.
from flask import Flask, request
app = Flask(__name__)


@app.route('/add')
def add():
    """
    Add a and b.
    http://127.0.0.1:5000/add?a=5&b=3
    """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a + b)


@app.route('/sub')
def sub():
    """
    Substract b from a.
    http://127.0.0.1:5000/sub?a=5&b=3
    """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a - b)


@app.route('/mult')
def mult():
    """
    Multiply a and b.
    http://127.0.0.1:5000/mult?a=5&b=3
    """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a * b)


@app.route('/div')
def div():
    """
    Divide a by b.
    http://127.0.0.1:5000/div?a=15&b=3
    """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a / b)


if __name__ == '__main__':
    app.debug = True
    app.run()
