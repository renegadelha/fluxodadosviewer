from flask import Flask, render_template
from flask_socketio import SocketIO
import random

app = Flask(__name__)
#se for para receber dados so sensor, tem que trocar threading por eventlet. acho que só precisa isso
socketio = SocketIO(app, async_mode='threading')

@app.route('/')
def index():
    return render_template('index2.html')


'''
@app.route('/receberdado', methods=['POST'])
def receber_dado():
    dado = ...
    socketio.emit('temperatura', {'value': dado})
'''

def gerar_dados():
    while True:
        temp = random.uniform(20.0, 30.0)
        socketio.emit('temperatura', {'value': round(temp, 2)})
        socketio.sleep(1)


if __name__ == '__main__':
    socketio.start_background_task(gerar_dados)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
