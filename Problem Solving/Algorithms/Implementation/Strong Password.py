#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_numbers = False
    has_lower_case = False
    has_upper_case = False
    has_special_characters = False
    
    for char in password:
        if char in numbers:
            has_numbers = True
        elif char in lower_case:
            has_lower_case = True
        elif char in upper_case:
            has_upper_case = True
        elif char in special_characters:
            has_special_characters = True

    count = 0
    if has_numbers is False:
        count += 1
    if has_lower_case is False:
        count += 1
    if has_upper_case is False:
        count += 1
    if has_special_characters is False:
        count += 1

    if len(password) + count < 6:
        return 6 - len(password)
    return count





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
