#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    ord_dif_s, ord_dif_rev_s = [], []
    n = len(s)
    for i in range(n - 1):
        ord_dif_s.append(abs(ord(s[i]) - ord(s[i + 1])))
        rev_idx = n - i - 1
        ord_dif_rev_s.append(abs(ord(s[rev_idx]) - ord(s[rev_idx - 1])))

    if ord_dif_rev_s == ord_dif_s:
        return "Funny"
    return "Not Funny"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
