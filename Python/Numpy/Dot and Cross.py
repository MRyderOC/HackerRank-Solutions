import numpy as np

N = int(input())

A = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for _ in range(N)])
B = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for _ in range(N)])

print(np.dot(A, B))
