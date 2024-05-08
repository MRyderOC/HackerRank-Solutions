#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s):
    # Write your code here
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        return "Empty String"
    return "".join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
