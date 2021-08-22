import numpy as np

M, N = list(map(int, input().split()))

arr = np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N)])

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.around(np.std(arr), decimals=11))
