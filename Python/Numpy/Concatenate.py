import numpy as np

N, M, P = list(map(int, input().split()))

print(np.concatenate([np.array(list(map(int, input().split())), ndmin=2) for i in range(N+M)]))
