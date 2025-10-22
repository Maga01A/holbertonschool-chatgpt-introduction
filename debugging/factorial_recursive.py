#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Compute the factorial of a non-negative integer n using recursion.
        The factorial of n (n!) is the product of all positive integers less than
        or equal to n. By definition, 0! == 1.

    Parameters:
        n (int): Non-negative integer whose factorial to compute.

    Returns:
        int: The factorial of n (n!). For n == 0 this returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
