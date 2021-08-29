import math

def cdf_normal_distro(x, mean, std):
    return 1/2 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

max_weight = int(input())
n = int(input())
mean = int(input())
std = int(input())

new_mean = mean * n
new_std = std * (n ** (1/2))

print(f'{round(cdf_normal_distro(max_weight, new_mean, new_std), 4):.4f}')
