import numpy as np

M, N = list(map(int, input().split()))

arr = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N)])

print(np.max(np.min(arr, axis=1)))
