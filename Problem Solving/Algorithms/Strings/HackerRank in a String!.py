#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    h_idx = 0
    h_str = "hackerrank"
    s_idx = 0
    while s_idx < len(s) and h_idx < len(h_str):
        if s[s_idx] == h_str[h_idx]:
            h_idx += 1
        s_idx += 1

    if h_idx == len(h_str):
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
