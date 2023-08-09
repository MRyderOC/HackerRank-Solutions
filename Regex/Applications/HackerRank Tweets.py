import re

regex_pattern = r"hackerrank"

count = 0
n = int(input())
for _ in range(n):
    row_input = input()
    if re.search(regex_pattern, row_input, re.IGNORECASE):
        count += 1

print(count)
