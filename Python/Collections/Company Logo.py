#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    c = Counter(s)
    l = sorted(list(c.items()), key=lambda item: (c.most_common(1)[0][1] - item[1], item[0]))
    for i in range(3):
        print(f'{l[i][0]} {l[i][1]}')
