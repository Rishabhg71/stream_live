from flask import Flask, jsonify, render_template, Response,request
from flask_socketio import SocketIO
import traceback

#Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/auth',methods=['POST'])
def auth():
    data = request
    print(data)
    try:
        return jsonify({"msg":"success"},200)
    except:
        traceback.print_exc()
    # return "HELLO WORLD"

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


if __name__ == '__main__':
    # socketio.run(app)
    app.run(debug=True,host='0.0.0.0',port=8000)