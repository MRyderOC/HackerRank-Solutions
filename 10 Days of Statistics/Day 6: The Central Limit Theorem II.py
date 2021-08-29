import math

def cdf_normal_distro(x, mean, std):
    return 1/2 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

mins = int(input())
n = int(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = std * (n ** (1/2))

print(f'{round(cdf_normal_distro(mins, new_mean, new_std), 4):.4f}')
