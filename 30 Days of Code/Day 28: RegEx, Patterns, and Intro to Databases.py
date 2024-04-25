#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    gmail_pattern = "^.*@gmail[.]com$"
    gmail_owners = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        regex_flag = re.search(gmail_pattern, emailID)
        if not regex_flag:
            continue

        gmail_owners.append(firstName)

print("\n".join(sorted(gmail_owners)))
