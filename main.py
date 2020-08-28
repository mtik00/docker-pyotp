#!/usr/bin/env python3
import sys
import pyotp
import time

if len(sys.argv) < 2:
    print("Usage: pyotp <OTP secret>")
    sys.exit(1)

secret = sys.argv[-1]

totp = pyotp.TOTP(secret)

print("Current OTP:", totp.now())

expires = int(30 - time.time() % 30)
print(f" expires in: {expires}s")
