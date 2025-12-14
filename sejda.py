from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- add this

app = Flask(__name__)
CORS(app)


@app.route('/licenses/verify', methods=['POST'])
def check_license():

    # 2. Always return the success response
    return jsonify({
        "reason": "Your license is active",
        "code": "ok"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)