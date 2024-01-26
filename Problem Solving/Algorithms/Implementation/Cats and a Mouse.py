#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    dist_cat_a = abs(x - z)
    dist_cat_b = abs(y - z)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    return "Cat B" if dist_cat_a > dist_cat_b else "Cat A"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
