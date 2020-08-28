#!/usr/bin/env python3
import sys
import time

import pyotp

if len(sys.argv) < 2:
    print("Usage: pyotp <OTP secret>")
    sys.exit(1)

secret = sys.argv[-1]

# Never show `0` seconds; it's pretty pointless
expires = int(30 - time.time() % 30)
while not expires:
    time.sleep(0.5)
    expires = int(30 - time.time() % 30)

totp = pyotp.TOTP(secret)

print(totp.now(), f"({expires}s)")
