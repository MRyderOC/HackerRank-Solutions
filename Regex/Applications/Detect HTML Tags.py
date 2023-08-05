import re

tag_pattern = r"(?<=<)\s*(\w+)"

results = []
n = int(input())
for _ in range(n):
    row_input = input()
    results.extend(re.findall(tag_pattern, row_input))

print(";".join(sorted(list(set(results)))))
