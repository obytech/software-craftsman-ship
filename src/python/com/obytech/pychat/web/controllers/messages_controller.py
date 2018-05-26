import datetime
from com.obytech.pychat.dtos.message import Message
from com.obytech.pychat.managers.messages_repo import add_message, get_messages

from flask import Flask, make_response
from flask import request

app = Flask(__name__)
endpoint = '/message'


@app.route(endpoint + '/send', methods=['POST'])
def send_message():
    json = request.get_json()
    message = Message(datetime.datetime.now(), json['src'], json['dst'], json['body'])
    add_message(message)

    return make_response()


@app.route(endpoint + '/<id>/sync/<int:timestamp>', methods=['POST'])
def sync(id, timestamp):
    datetime.datetime.fromtimestamp(timestamp)
    msgs = get_messages(id, timestamp)
    resp = make_response(str(msgs))
    resp.mimetype = "application/json"
    return resp


