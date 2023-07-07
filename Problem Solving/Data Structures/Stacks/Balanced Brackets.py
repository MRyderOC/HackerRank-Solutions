#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    for ch in s:
        if ch in ['(', '{', '[']:
            stack.append(ch)
        elif ch in [')', '}', ']']:
            if not stack:
                return 'NO'

            top = stack[-1]
            if ch == ')' and top == '(':
                stack.pop()
            elif ch == ']' and top == '[':
                stack.pop()
            elif ch == '}' and top == '{':
                stack.pop()
            else:
                stack.append(ch)

    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

