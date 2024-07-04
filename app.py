from flask import Flask, request, jsonify
import africastalking
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Africa's Talking SDK
africastalking.initialize(app.config['AT_USERNAME'], app.config['AT_API_KEY'])
sms = africastalking.SMS


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')

    try:
        response = sms.send(message, [phone_number])
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
