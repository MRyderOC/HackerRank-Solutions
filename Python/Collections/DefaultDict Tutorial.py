from collections import defaultdict

n, m = list(map(int, input().split()))
A = defaultdict(list)

i = 0
while i < n:
    line = input()
    A[line].append(i+1)
    i += 1

while i < m+n:
    line = input()
    out = A[line]
    if out != []:
        print(' '.join(map(str, out)))
    else:
        print('-1')
    i += 1

