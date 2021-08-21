import numpy as np

dims = list(map(int, input().split()))

print(np.zeros(tuple(dims), dtype=np.int32))
print(np.ones(tuple(dims), dtype=np.int32))
