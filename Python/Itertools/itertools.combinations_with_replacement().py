from itertools import combinations_with_replacement

inp = input().split()

print('\n'.join(sorted([''.join(map(str, sorted(item))) for item in combinations_with_replacement(inp[0], int(inp[1]))])))
