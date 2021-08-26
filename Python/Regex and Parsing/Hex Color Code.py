import re


for _ in range(int(input())):
    m = re.findall(r'(#[\dA-Fa-f]{6}|#[\dA-Fa-f]{3})[^\n|\s+{]', input())
    if m:
        print('\n'.join(m))
