#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        multiple_input = input().rstrip().split()
        n = int(multiple_input[0])
        k = int(multiple_input[1])

        the_min = min(k, n - k - 1)
        ind = the_min * 2
        if k == the_min:
            ind += 1
        if n % 2 == 1 and k == n // 2:
            ind = n - 1

        print(ind)
