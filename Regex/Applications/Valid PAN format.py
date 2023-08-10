import re

regex_pattern = r"^[A-Z]{5}\d{4}[A-Z]$"

n = int(input())
for _ in range(n):
    row_input = input()
    result = "YES" if re.search(regex_pattern, row_input) else "NO"
    print(result)
