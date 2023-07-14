#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False

    return True


def primeCount(n):
    # Write your code here
    if n == 1:
        return 0

    prime_list = [i for i in range(2, 101) if is_prime(i)]
    qq = 1
    i = 0
    while qq < n:
        qq *= prime_list[i]
        i += 1

    if qq > n:
        return i - 1
    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
