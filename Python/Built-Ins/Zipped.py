N, X = list(map(int, input().split()))

for student in zip(*[list(map(float, input().split())) for i in range(X)]):
    print(sum(student)/X)
