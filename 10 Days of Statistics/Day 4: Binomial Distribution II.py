from math import comb

def binomial_distro(x, n, p):
    return comb(n, x) * (p ** x) * ((1-p) ** (n-x))

p , n = list(map(int, input().split()))

s1 = sum([binomial_distro(i, n, p/100) for i in range(3)])
s2 = sum([binomial_distro(i, n, p/100) for i in range(2,11)])
    
print(f'{round(s1, 3):.3f}\n{round(s2, 3):.3f}')
