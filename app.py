from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, it is simple massage. Add /api/data to get more opportunities"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Congrats, you finally received this message!!!',
        'next step': 'Also try POST to send json to customize received message',
        'hint': '(Body - raw  json - write message - send)'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    response = {
        'message': 'You received customized message!',
        'customized message': new_data,
        'hint': '(also try GET, you don`t need to write anything there)'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
