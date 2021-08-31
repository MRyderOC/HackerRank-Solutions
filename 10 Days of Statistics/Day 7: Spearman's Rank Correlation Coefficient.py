def rank(l, n):
    return [sorted(l).index(l[i])+1 for i in range(n)]

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

d = sum([(x-y)**2 for x, y in zip(rank(X, n), rank(Y, n))])

print(f'{round(1 - (6 * d / (n * ((n ** 2) - 1))), 3):.3f}')
