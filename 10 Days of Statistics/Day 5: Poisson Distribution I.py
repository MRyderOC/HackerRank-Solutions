import math

def poisson_distro(k , l):
    return (l ** k) * (math.e ** (-l)) / (math.factorial(k))

m = float(input())
k = int(input())

print(f'{round(poisson_distro(k, m), 3):.3f}')
