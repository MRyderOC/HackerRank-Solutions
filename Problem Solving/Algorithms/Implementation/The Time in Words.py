#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


def timeInWords(h, m):
    # Write your code here
    number_word_map = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "half"
    }

    hour, mins = number_word_map[h], number_word_map.get(m)
    if m == 0:
        return f"{hour} o' clock"
    elif m == 1:
        return f"{mins} minute past {hour}"
    elif m == 15 or m == 30:
        return f"{mins} past {hour}"
    elif m < 30:
        if m > 20:
            mins = f"{number_word_map[20]} {number_word_map[m % 10]}"

        return f"{mins} minutes past {hour}"
    elif m > 31:
        res = 60 - m
        hour, mins = number_word_map[h + 1], number_word_map.get(res)
        if res == 1:
            return f"{mins} minute to {hour}"
        elif res == 15:
            return f"{mins} to {hour}"
        else:
            if res > 20:
                mins = f"{number_word_map[20]} {number_word_map[res % 10]}"

            return f"{mins} minutes to {hour}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
