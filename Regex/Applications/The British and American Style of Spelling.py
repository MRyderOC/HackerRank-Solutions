import re

n = int(input())
s = " ".join([input() for _ in range(n)])
t = int(input())
for _ in range(t):
    test_case = input()
    am_pattern = rf"{test_case[:-2]}ze"
    br_pattern = rf"{test_case[:-2]}se"

    print(len(re.findall(rf"{am_pattern}|{br_pattern}", s)))
