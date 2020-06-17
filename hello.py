#!/usr/bin/python

from flask import Flask, make_response
from gevent.pywsgi import WSGIServer
import http
import signal
import sys

def handle_signal(signum, frame):
    print('Stopping process... (signal {})'.format(signum))
    sys.exit(0)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return make_response('Hello World!', http.HTTPStatus.OK)

@app.route('/<path>')
def other_page(path):
    return make_response('The requested URL /{} was not found on this server'.format(path), http.HTTPStatus.NOT_FOUND)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()

# new line
