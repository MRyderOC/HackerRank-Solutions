import re

regex_pattern = r"^[hH][iI]\s[^dD]\w*"

n = int(input())
for _ in range(n):
    s = input()
    if re.search(regex_pattern, s):
        print(s)
