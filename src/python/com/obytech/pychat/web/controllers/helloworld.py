from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello')
def hello():
    if request.method == 'GET':
        print('get')
    print(request.args.get('param', None))
    return hello_x(request.args.get('param', 'world'))


def hello_x(x="world"):
    return "Hello, " + x
