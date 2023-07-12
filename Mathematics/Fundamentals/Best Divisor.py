#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict



if __name__ == '__main__':
    n = int(input().strip())
    is_divisor = lambda n, i: True if n % i == 0 else False
    sum_of_digits = lambda x: sum(map(int, list(str(x))))

    div_sum_dict = defaultdict(list)
    for i in range(1, n + 1):
        if is_divisor(n, i):
            div_sum_dict[sum_of_digits(i)].append(i)

    max_sum_list = div_sum_dict[max(div_sum_dict.keys())]
    best_divisor = min(max_sum_list)
    print(best_divisor)
