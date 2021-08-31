from itertools import groupby


out = [(len(list(g)), int(k)) for k, g in groupby(input())]
for item in out:
    print(f'{item} ', end='')

