import random
OTP = None  
def randomOTP():
    global OTP  
    if OTP is None:  
        OTP = random.randint(100000, 999999)
    return OTP
