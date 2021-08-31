import numpy as np

m, n = list(map(int, input().split()))

X = []
Y = []
for i in range(n):
    line = list(map(float, input().split()))
    X.append([1] + line[:-1])
    Y.append(line[-1])

q = int(input())
Q = []
for i in range(q):
    Q.append([1] + list(map(float, input().split())))

X = np.array(X)
Y = np.array(Y)
B = np.linalg.inv(X.T @ X) @ X.T @ Y

Q = np.array(Q)

for num in (Q@B):
    print(f'{round(num, 2):.2f}')
