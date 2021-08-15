from itertools import combinations

inp = input().split()

for i in range(1, int(inp[1])+1):
    print('\n'.join(sorted([''.join(map(str, sorted(item))) for item in combinations(inp[0], i)])))
