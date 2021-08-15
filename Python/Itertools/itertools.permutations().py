from itertools import permutations

inp = input().split()
print('\n'.join(sorted([''.join(map(str, item)) for item in permutations(inp[0], int(inp[1]))])))
