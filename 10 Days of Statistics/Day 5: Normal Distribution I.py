import math

def cdf_normal_distro(x, mean, std):
    return 1/2 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))
    

mean, std = list(map(float, input().split()))
q1 = float(input())
l, u = list(map(float, input().split()))

print(f'{round(cdf_normal_distro(q1, mean, std), 3):.3f}')
print(f'{round(cdf_normal_distro(u, mean, std) - cdf_normal_distro(l, mean, std), 3):.3f}')
