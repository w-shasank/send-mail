from flask import Flask, request, jsonify
from flask_cors import CORS
from Sendmail import Tosend_il
from OTPgenerate import randomOTP
name='shashank'
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

otp_storage = {}  # Dictionary to store OTPs for verification

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json
    recipient = data.get("email")
    address=data.get("address")
    name=data.get("name")
    
    if not recipient:
        return jsonify({"error": "Email is required"}), 400

    otp = randomOTP()
    otp_storage[recipient] = otp  # Store OTP for later verification

    Tosend_il(recipient)  # Send the OTP email
    return jsonify({"message": "OTP sent successfully!   "+name+"  "+address+"  "+str(otp)})



#checking and returning the status
@app.route('/verify-otp', methods=['GET'])
def verify_otp():
    recipient = request.args.get("email")
    user_otp = request.args.get("otp")

    if not recipient or not user_otp:
        return jsonify({"status": 2}), 400

    try:
        user_otp = int(user_otp)
    except ValueError:
        return jsonify({"status": 2}), 400

    if otp_storage.get(recipient) == user_otp:
        return jsonify({"status": 1})  # success
    else:
        return jsonify({"status": 0}), 401  # failure



if __name__ == '__main__':
    app.run(debug=True)

