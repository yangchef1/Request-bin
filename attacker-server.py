from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

waiting_request = None
waiting_thread = None

def send_flag_response(flag):
    with app.app_context():
        if waiting_request:
            print(f"flag가 전송되었습니다. : {flag}")
            waiting_thread.result = flag
            waiting_request = False 

@app.route('/get_flag', methods=['GET'])
def get_flag():
    global waiting_request
    print("Waiting for flag...")

    waiting_request = True
    waiting_thread = threading.local()
    waiting_thread.result = None

    while waiting_request:
        pass

    return jsonify({"flag": waiting_thread.result}), 200

@app.route('/recieve_cookie', methods=['GET'])
def recieve_cookie():
    flag = request.args.get('flag')
    print(f"서버가 flag를 수신했했습니다. : {flag}")
    
    if not flag:
      print("잘못된 flag 입니다.")
      return

    threading.Thread(target=send_flag_response, args=(flag,)).start()
    return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
