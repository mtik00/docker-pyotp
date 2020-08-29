#!/usr/bin/env python3
import argparse
import sys
import time
from typing import List

import pyotp


def parse_args(args: List[str] = sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("secret", help="The secret token to use for code generation")
    parser.add_argument(
        "-c", "--continuous", help="Continually output the code", action="store_true"
    )
    parser.add_argument(
        "-i", "--interval", help="The TOTP interval", type=int, default=30
    )
    return parser.parse_args(args)


def expiration(period: int = 30, wait: bool = False) -> int:
    """Returns the number of seconds until the current code expires."""
    expiration = int(period - time.time() % period)

    if wait:
        while not expiration:
            expiration = int(period - time.time() % period)

    return expiration


def show_code(secret: str, interval: int = 30, wait: bool = False) -> str:
    """Converts the secret and the interval into the current TOTP code."""
    totp = pyotp.TOTP(secret, interval=interval)
    expires = expiration(interval, wait)
    return f"{totp.now()} ({expires!s:>2}s)"


def continuous(secret: str, interval: int) -> None:
    """Continuously display the current token."""

    try:
        while True:
            print(show_code(secret, interval), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        # Print out the final code on a new line
        print()
        print(show_code(secret, interval))


def single(secret: str, interval: int) -> None:
    """Show only the current token."""
    print(show_code(secret, interval, wait=True))


def main():
    args = parse_args()

    if args.continuous:
        continuous(args.secret, args.interval)
    else:
        single(args.secret, args.interval)


if __name__ == "__main__":
    main()
