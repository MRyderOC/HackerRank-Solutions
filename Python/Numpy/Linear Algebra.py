import numpy as np

A = np.concatenate([np.array(list(map(float, input().split())), ndmin=2) for _ in range(int(input()))])
print(round(np.linalg.det(A), 2))
