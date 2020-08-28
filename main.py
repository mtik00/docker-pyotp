#!/usr/bin/env python3
import sys
import time

import pyotp

if len(sys.argv) < 2:
    print("Usage: pyotp <OTP secret>")
    sys.exit(1)

secret = sys.argv[-1]

totp = pyotp.TOTP(secret)

expires = int(30 - time.time() % 30)
print(totp.now(), f"({expires}s)")
