def mean(arr): return sum(arr) / len(arr)

def stdev(arr):
    m = mean(arr)
    return (sum([(item - m)**2 for item in arr])/len(arr)) ** 0.5

def corr(X, Y, n):
    mean_X = mean(X)
    mean_Y = mean(Y)
    std_X = stdev(X)
    std_Y = stdev(Y)

    cov = 0
    for i in range(n):
        cov += (X[i] - mean_X) * (Y[i] - mean_Y)

    return cov / (std_X * std_Y * n)


x = []
y = []
for i in range(5):
    x1, y1 = list(map(int, input().split()))
    x.append(x1)
    y.append(y1)

b = corr(x, y, len(x)) * (stdev(y) / stdev(x))
a = mean(y) - b * mean(x)

print(f'{round(b * 80 + a, 3):.3f}')
