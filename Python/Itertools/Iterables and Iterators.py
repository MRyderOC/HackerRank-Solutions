from itertools import combinations


N = int(input())
l = input().split()
k = int(input())


out = round(1 - (len(list(combinations(['z'] * (len(l) - l.count('a')), k))) / len(list(combinations(l, k)))), 3)

print(f'{out:.3f}')
