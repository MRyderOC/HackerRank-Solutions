#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    topic_known, teams = 0, 0
    for p1, p2 in combinations(topic, 2):
        tmp_topic_known = 0
        for ch1, ch2 in zip(p1, p2):
            if ch1 == "1" or ch2 == "1":
                tmp_topic_known += 1
        # res = int(p1) | int(p2)
        # tmp_topic_known = sum(list(map(int, list(str(res)))))
        if tmp_topic_known > topic_known:
            topic_known = tmp_topic_known
            teams = 1
        elif tmp_topic_known == topic_known:
            teams += 1

    return [topic_known, teams]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
