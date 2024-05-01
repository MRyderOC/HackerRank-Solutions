#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    # Write your code here
    if len(s) == 0 or s[0] == 0:
        print("NO")
        return

    flag = False
    k = 1
    while k <= (len(s) / 2) + 1:
        n = int(s[:k])
        tmp = str(n)
        i = 1
        while len(tmp) < len(s):
            tmp += str(n + i)
            i += 1

            if tmp == s:
                flag = True
                break
        if flag:
            break

        k += 1

    if flag:
        print(f"YES {n}")
    else:
        print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
