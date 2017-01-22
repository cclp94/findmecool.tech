import socket,os
import sys
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from flask import Flask
from bot import queryTopTrend
app = Flask(__name__)

UDP_PORT = 5000
UDP_IP = "127.0.0.1"
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/test")
@crossdomain(origin='*')
def test():
    return queryTopTrend()

class Socket:
    #udp socket
    msg = ""
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
        print("socket created")
    except:
        print ("Failed to create socket")
        sys.exit()
    # Bind socket to local host and port
    try:
        sock.bind((UDP_IP, UDP_PORT))
    except:
        print ("Bind failed")
        sys.exit()
         
    print ('Socket bind complete')   

    while True:
        data, addr = sock.recvfrom(1024)
        print ("received message: ", data)

    sock.close()

if __name__ == '__main__':
    app.run()
    Socket()

