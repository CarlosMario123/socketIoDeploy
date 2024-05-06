from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*')

@socketio.on('mensaje')
def handle_message(data):
    print('Mensaje recibido: ' + data)
    socketio.emit('controlar', data)


@socketio.on("recibirInfo")
def reciveMensaje(data):
    socketio.emit("recibirInfo",data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000)

