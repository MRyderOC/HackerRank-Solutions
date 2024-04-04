#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_hourglass = -64
    for j in range(4):
        for i in range(4):
            tmp_hg = [
                arr[j][i], arr[j][i + 1], arr[j][i + 2],
                arr[j + 1][i + 1],
                arr[j + 2][i], arr[j + 2][i + 1], arr[j + 2][i + 2],
            ]
            max_hourglass = max(max_hourglass, sum(tmp_hg))

    print(max_hourglass)
