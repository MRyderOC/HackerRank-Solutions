num, denom = list(map(int, input().split()))
p = num / denom
n = int(input())

def geo_distro(n,p): return ((1-p)**(n-1)) * p

s = sum([geo_distro(i, p) for i in range(1,6)])

print(f'{round(s, 3):.3f}')
