from flask import Flask, render_template, request, jsonify
#from flask_socketio import SocketIO, join_room, emit, send
from flask_uwsgi_websocket import GeventWebSocket
from copy import deepcopy
import time

DefaultResponse = {
    'code': 20000,
    'data': None
}


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DEBUG=True
    )

    ws = GeventWebSocket(app)

    users = {}

    print("in create applicaton")

    @app.route('/')
    def index():
        print("try to render index")
        return render_template('index.html')

    @app.route('/msg')
    def sendmsg():
        res = deepcopy(DefaultResponse)

        print("in msg")

        msg = request.args.get("cmd")

        print("get msg: " + msg)

        for id in users:
            print("send msg to " + str(id))
            users[id].send(msg)

        return jsonify(res)


    @ws.route('/websocket')
    def chat(ws):
        users[ws.id] = ws

        #for msg in backlog:
            #ws.send(msg)

        while True:
            msg = ws.receive()

            print("recv websocket msg: " + str(msg))

            #time.sleep(10)

            if msg is not None:
                #backlog.append(msg)
                for id in users:
                    if id != ws.id:
                        users[id].send(msg)


            else:
                break

        #del users[ws.id]


    return app

if __name__ == '__main__':
    #socketio.run(app, debug=True)
    application.run()
