from collections import Counter

c = Counter([input() for i in range(int(input()))])

print(len(c))
[print(c[item], end=' ') for item in c]
