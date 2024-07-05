import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # Process the webhook payload
    payload = request.json
    print(payload)  # or do something with the payload
    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
