import re

regex_pattern = r"^[a-z]{0,3}\d{2,8}[A-Z]{3,}$"

n = int(input())
for _ in range(n):
    row_input = input()
    if re.search(regex_pattern, row_input):
        print("VALID")
    else:
        print("INVALID")
