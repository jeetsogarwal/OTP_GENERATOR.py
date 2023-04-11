import random,math
def generateOTP():
    otp = ""
    for i in range(1,5):
        a=random.random()
        b=math.floor(a*10)
        otp = otp+str(b)
    return otp
print("Your OTP is: ",generateOTP())

