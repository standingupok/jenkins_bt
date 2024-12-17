from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Lấy version của ứng dụng
@app.route('/get_version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0.0", "status": "success"})

# Route 2: Kiểm tra số nguyên tố
@app.route('/', methods=['GET'])
def check_prime():
    try:
        number = int(request.args.get("number", "0"))
        if number < 2:
            return jsonify({"number": number, "is_prime": False})
        
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return jsonify({"number": number, "is_prime": False})
        
        return jsonify({"number": number, "is_prime": True})
    except ValueError:
        return jsonify({"error": "Invalid input, please provide an integer"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
