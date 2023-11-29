#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def single_grade(grade):
    if grade < 38 or grade % 5 == 0:
        return grade

    next_mult_5 = ((grade // 5) + 1) * 5
    if (next_mult_5 - grade) < 3:
        return next_mult_5
    return grade

def gradingStudents(grades):
    # Write your code here
    return [single_grade(g) for g in grades]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
