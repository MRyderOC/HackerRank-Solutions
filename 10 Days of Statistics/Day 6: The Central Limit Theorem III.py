n = int(input())
mean = float(input())
std = float(input())
prcntg = float(input())
z = float(input())

new_std = std / (n ** (1/2))
print(f'{round(mean - z * new_std, 2):.2f}')
print(f'{round(mean + z * new_std, 2):.2f}')
