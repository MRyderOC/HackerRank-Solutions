import re

n = int(input())
words = []
for _ in range(n):
    words.extend(input().split())

t = int(input())
for _ in range(t):
    br_test_case = input()
    am_test_case = br_test_case.replace("our", "or")
    pattern = rf"^{br_test_case}$|^{am_test_case}$"

    print(sum(list(map(lambda val: 1 if re.search(pattern, val.strip()) else 0, words))))
