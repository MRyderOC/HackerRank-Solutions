#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    distances = [0] * n
    for i in range(c[0] + 1):
        distances[i] = c[0] - i

    station_idx_1, station_idx_2 = 0, 1
    for city_idx in range(c[0] + 1, c[-1]):
        if city_idx == c[station_idx_2]:
            station_idx_1 += 1
            station_idx_2 += 1
            continue
        distances[city_idx] = min(
            abs(city_idx - c[station_idx_2]),
            abs(city_idx - c[station_idx_1]))

    for i in range(c[-1], n):
        distances[i] = i - c[-1]

    return max(distances)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
