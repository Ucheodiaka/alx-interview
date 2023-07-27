#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates
    the fewest number of operations needed to result
    exactly n H characters in the file.
    """

    bd = 1
    start = 0
    op = 0
    while bd < n:
        remainder = n - bd
        if (remainder % bd == 0):
            st = bd
            bd += st
            op += 2
        else:
            bd += st
            op += 1
    return op
