#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valeys = 0
    alt = 0
    for item in path:
        was_in_sea_level = alt == 0
        if item == "D":
            alt -= 1
        elif item == "U":
            alt += 1

        if was_in_sea_level and alt < 0:
            valeys += 1

    return valeys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
