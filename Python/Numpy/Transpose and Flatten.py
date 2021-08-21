import numpy as np

N, M = list(map(int, input().split()))

arr = np.array([list(map(int, input().split())) for i in range(N)])

print(np.transpose(arr))
print(arr.flatten())
