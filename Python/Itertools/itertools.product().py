from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(' '.join(list(map(str, product(A, B)))))

