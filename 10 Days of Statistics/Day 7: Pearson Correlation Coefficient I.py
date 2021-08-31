def stdev(arr):
    mean = sum(arr)/len(arr)
    return (sum([(item - mean)**2 for item in arr])/len(arr)) ** 0.5

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)
std_X = stdev(X)
std_Y = stdev(Y)

cov = 0
for i in range(n):
    cov += (X[i] - mean_X) * (Y[i] - mean_Y)


print(f'{round(cov / (std_X * std_Y * n), 3):.3f}')
