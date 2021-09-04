from itertools import product

K, M = list(map(int, input().split()))
l = [list(map(lambda x: int(x) ** 2, input().split()[1:])) for i in range(K)]
print(max([sum(item)%M for item in product(*l)]))
