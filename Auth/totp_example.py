import pyotp
import time

totp = pyotp.TOTP(pyotp.random_base32())
for x in range(0, 60):
    print("Current OTP:", totp.now())
    time.sleep(1)
