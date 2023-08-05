import re

username_pattern = r"^[_|.]\d+[a-zA-Z]*_?$"

n = int(input())

for _ in range(n):
    row_input = input()
    if re.search(username_pattern, row_input):
        print("VALID")
    else:
        print("INVALID")
