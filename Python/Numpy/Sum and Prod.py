import numpy as np

N, M = list(map(int, input().split()))

arr = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N)])

print(np.prod(np.sum(arr, axis=0)))
