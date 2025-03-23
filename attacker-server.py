from flask import Flask, request, jsonify
import time

app = Flask(__name__)

waiting_request = None

@app.route('/get_flag', methods=['GET'])
def get_flag():
    global waiting_request
    print("Waiting for flag to be received...")
    waiting_request = request
    return "Waiting for flag..."

@app.route('/recieve_cookie', methods=['GET'])
def recieve_cookie():
    global waiting_request
    flag = request.args.get('flag')

    if flag and waiting_request:
        print(f"Received flag: {flag}")
        return jsonify({"flag": flag}), 200
    elif not flag:
        return jsonify({"error": "No flag received"}), 400
    else:
        return jsonify({"error": "No waiting request found"}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
