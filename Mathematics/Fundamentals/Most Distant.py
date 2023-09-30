#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    neg_x, neg_y, pos_x, pos_y = 0, 0, 0, 0
    for cor in coordinates:
        if cor[0] > pos_x:
            pos_x = cor[0]
        elif cor[0] < neg_x:
            neg_x = cor[0]

        if cor[1] > pos_y:
            pos_y = cor[1]
        elif cor[1] < neg_y:
            neg_y = cor[1]

    x_dist = abs(neg_x - pos_x)
    y_dist = abs(neg_y - pos_y)
    sqrt_calc = lambda x, y: ((x ** 2) + (y ** 2)) ** (1 / 2)
    first_sqrt = sqrt_calc(pos_x, pos_y)
    second_sqrt = sqrt_calc(neg_x, pos_y)
    third_sqrt = sqrt_calc(neg_x, neg_y)
    fourth_sqrt = sqrt_calc(pos_x, neg_y)
    
    return max([
        x_dist, y_dist, first_sqrt, second_sqrt, third_sqrt, fourth_sqrt,
    ])






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
