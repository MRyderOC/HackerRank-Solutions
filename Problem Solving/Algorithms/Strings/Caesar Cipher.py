#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase
from string import ascii_uppercase
from itertools import chain
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    new_lower = ascii_lowercase[k:] + ascii_lowercase[:k]
    new_upper = ascii_uppercase[k:] + ascii_uppercase[:k]
    chain_iter = chain(
        zip(ascii_lowercase, new_lower),
        zip(ascii_uppercase, new_upper))

    letter_map = {old: new for old, new in chain_iter}
    out = []
    for ch in s:
        if tmp := letter_map.get(ch):
            out.append(tmp)
        else:
            out.append(ch)
    return "".join(out)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
