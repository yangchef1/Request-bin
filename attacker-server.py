from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

is_waiting = True
flag = ""

@app.route('/get_flag', methods=['GET'])
def get_flag():
    global is_waiting
    print("Waiting for flag...")

    while is_waiting:
        pass

    return jsonify({"flag": flag}), 200

@app.route('/recieve_cookie', methods=['GET'])
def recieve_cookie():
    global flag, is_waiting
    flag = request.args.get('flag')
    print(f"서버가 flag를 수신했했습니다. : {flag}")
    
    if not flag:
      print("잘못된 flag 입니다.")
      return jsonify({"message": "failed"}), 400

    is_waiting = False
    return jsonify({"message": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
