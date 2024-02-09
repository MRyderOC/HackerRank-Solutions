#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def is_kaprekar(n):
    if n == 1:
        return True

    digits = len(str(n))
    n_squared = n ** 2
    first_half_str = str(n_squared)[:-digits]
    secon_half_str = str(n_squared)[-digits:]
    first_half = 0 if not first_half_str else int(first_half_str)
    secon_half = 0 if not first_half_str else int(secon_half_str)
    if first_half + secon_half == n:
        return True
    return False

def kaprekarNumbers(p, q):
    # Write your code here
    out = [
        i
        for i in range(p, q + 1)
        if is_kaprekar(i)
    ]

    if out:
        print(" ".join(list(map(str, out))))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
