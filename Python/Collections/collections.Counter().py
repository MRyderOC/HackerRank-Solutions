from collections import Counter

X = int(input())
sizes = Counter(list(map(int, input().split())))
N = int(input())
s = 0
for i in range(N):
    size, cost = list(map(int, input().split()))
    if sizes[size] != 0:
        s += cost
        sizes[size] -= 1
        
print(s)
