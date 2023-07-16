#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def halloweenParty(k):
    # Write your code here
    tmp = k // 2
    if k % 2 == 0:
        return tmp ** 2
    else:
        return tmp * (1 + tmp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        k = int(input().strip())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
