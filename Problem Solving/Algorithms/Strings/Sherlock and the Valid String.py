#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    the_counter = Counter(s)
    # print(the_counter)
    vals = set(list(the_counter.values()))
    if len(vals) == 1:
        return "YES"
    elif len(vals) >= 3:
        # print("l1")
        return "NO"
    else:  # len(vals) == 2
        vals_list = list(vals)
        if 1 in vals_list and len([item for item in the_counter.values() if item == 1]) == 1:
            return "YES"
        if abs(vals_list[0] - vals_list[1]) != 1:
            # print(f"l2: {vals_list}")
            return "NO"
        max_val = max(vals_list)
        if len([item for item in the_counter.values() if item == max_val]) == 1:
            return "YES"
        # print("l3")
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
