# Put your app in here.
from flask import Flask, request
app = Flask(__name__)


@app.route('/math/add')
def add():
    """
    Add a and b.
    http://127.0.0.1:5000/math/add?a=5&b=3
    """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a + b)


@app.route('/math/sub')
def sub():
    """
    Substract b from a.
    http://127.0.0.1:5000/math/sub?a=5&b=3
    """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a - b)


@app.route('/math/mult')
def mult():
    """
    Multiply a and b.
    http://127.0.0.1:5000/math/mult?a=5&b=3
    """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a * b)


@app.route('/math/div')
def div():
    """
    Divide a by b.
    http://127.0.0.1:5000/math/div?a=15&b=3
    """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a / b)


if __name__ == '__main__':
    app.debug = True
    app.run()
