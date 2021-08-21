import numpy as np

N, M = list(map(int, input().split()))

A = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N)])
B = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
