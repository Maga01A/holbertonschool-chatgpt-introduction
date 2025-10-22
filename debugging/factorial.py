#!/usr/bin/env python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # <-- fix: decrement n to avoid infinite loop
    return result

f = factorial(int(sys.argv[1]))
print(f)
