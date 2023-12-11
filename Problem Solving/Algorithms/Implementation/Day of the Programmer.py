#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def parse_julian_calendar(year):
    if year % 4 == 0:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

def parse_gregorian_calendar(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

def dayOfProgrammer(year):
    # Write your code here
    if year <= 1917:
        out = parse_julian_calendar(year)
    elif year == 1918:
        out = "26.09.1918"
    elif year >= 1919:
        out = parse_gregorian_calendar(year)

    return out





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
