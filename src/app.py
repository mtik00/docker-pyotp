#!/usr/bin/env python3
import argparse
import sys
import time
from typing import List

import pyotp
import pyperclip


def parse_args(args: List[str] = sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("secret", help="The secret token to use for code generation")
    parser.add_argument(
        "-c", "--continuous", help="Continually output the code", action="store_true"
    )
    parser.add_argument(
        "-i", "--interval", help="The TOTP interval", type=int, default=30
    )
    parser.add_argument(
        "--clipboard",
        help="Automatically copy the code to the clipboard",
        action="store_true",
    )
    return parser.parse_args(args)


def now(secret, interval):
    totp = pyotp.TOTP(secret, interval=interval)
    expires = expiration(interval)
    return totp.now(), expires


def expiration(period: int = 30, wait: bool = False) -> int:
    """Returns the number of seconds until the current code expires."""
    expiration = int(period - time.time() % period)

    if wait:
        while not expiration:
            expiration = int(period - time.time() % period)

    return expiration


def format_message(totp: str, expires: int, copied: bool = False):
    copied_message = " -- copied to clipboard" if copied else ""
    return f"{totp} ({expires!s:>2}s){copied_message}"


def continuous(secret: str, interval: int, clipboard: bool = False) -> None:
    """Continuously display the current token."""
    totp, expires = now(secret, interval)

    if clipboard:
        pyperclip.copy(totp)

    try:
        while True:
            current_totp = totp
            print(format_message(totp, expires, clipboard), end="\r")
            time.sleep(1)

            totp, expires = now(secret, interval)

            # Only copy the _new_ code to the clipboard to prevent constant
            # clipboard overwrites
            if clipboard and (current_totp != totp):
                pyperclip.copy(totp)
    except KeyboardInterrupt:
        # Print out the final code on a new line
        print()
        print(format_message(totp, expires, clipboard))


def single(secret: str, interval: int, clipboard: bool = False) -> None:
    """Show only the current token."""
    totp, expires = now(secret, interval)
    if clipboard:
        pyperclip.copy(totp)

    print(format_message(totp, expires, clipboard))


def main():
    args = parse_args()

    if args.continuous:
        continuous(args.secret, args.interval, clipboard=args.clipboard)
    else:
        single(args.secret, args.interval, clipboard=args.clipboard)


if __name__ == "__main__":
    main()
