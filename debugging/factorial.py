#!/usr/bin/env python3
import sys

def factorial(n):
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} N", file=sys.stderr)
        sys.exit(2)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: N must be an integer", file=sys.stderr)
        sys.exit(2)

    try:
        print(factorial(n))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
