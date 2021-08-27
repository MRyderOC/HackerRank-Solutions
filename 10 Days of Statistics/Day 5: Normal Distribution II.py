import math

def cdf_normal_distro(x, mean, std):
    return 1/2 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))
    

mean, std = list(map(float, input().split()))
q1 = float(input())
q2 = float(input())

print(f'{round(100*(1 - cdf_normal_distro(q1, mean, std)), 2):.2f}')
print(f'{round(100*(1 - cdf_normal_distro(q2, mean, std)), 2):.2f}')
print(f'{round(100*cdf_normal_distro(q2, mean, std), 2):.2f}')
