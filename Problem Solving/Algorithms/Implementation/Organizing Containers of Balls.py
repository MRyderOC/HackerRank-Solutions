#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#


def organizingContainers(container):
    # Write your code here
    containers_cap = []
    type_sum = [0] * len(container[0])

    for cont in container:
        containers_cap.append(sum(cont))
        for i, t in enumerate(cont):
            type_sum[i] += t

    if sorted(containers_cap) == sorted(type_sum):
        return "Possible"
    return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
