def EnterBody():
    from datautility import name  
    from OTPgenerate import randomOTP
    return f"Dear {name},\n\nThanks for logging in yout otp is :{randomOTP()}."

