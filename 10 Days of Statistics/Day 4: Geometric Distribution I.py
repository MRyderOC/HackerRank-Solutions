num, denom = list(map(int, input().split()))
p = num / denom
n = int(input())
def geo_distro(n,p): return ((1-p)**(n-1)) * p

print(f'{geo_distro(n, p):.3f}')
