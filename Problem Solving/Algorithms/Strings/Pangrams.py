#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase
from string import ascii_uppercase

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    letter_map = {" ": 26}
    for i in range(26):
        letter_map[ascii_lowercase[i]] = i
        letter_map[ascii_uppercase[i]] = i

    seen = [0] * 27
    for char in s:
        seen[letter_map[char]] = 1

    del seen[-1]
    if all(seen):
        return "pangram"
    return "not pangram"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
