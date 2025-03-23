from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

waiting_request = None

def send_flag_response(flag):
    with app.app_context():
        if waiting_request:
            print(f"Sending flag response to the receiver: {flag}")
            waiting_request = False 

@app.route('/get_flag', methods=['GET'])
def get_flag():
    global waiting_request
    print("Waiting for flag...")

    waiting_request = True

    while waiting_request:
        pass

    return jsonify({"message": "Flag received and sent to the receiver."}), 200

@app.route('/recieve_cookie', methods=['GET'])
def recieve_cookie():
    flag = request.args.get('flag')
    
    if not flag:
        return jsonify({"error": "No flag received"}), 400

    threading.Thread(target=send_flag_response, args=(flag,)).start()
    return jsonify({"message": "Flag received, response will be sent to the receiver."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
