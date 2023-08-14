import re

regex_pattern = r"^\([+-]?(90(\.0+)?|[1-8]?\d(\.\d+)?), [+-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d?\d(\.\d+)?)\)$"

n = int(input())
for _ in range(n):
    row_input = input()
    if re.search(regex_pattern, row_input):
        print("Valid")
    else:
        print("Invalid")
