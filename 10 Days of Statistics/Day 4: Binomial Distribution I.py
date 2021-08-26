from math import comb

s = 0
for i in range(3,7):
    s += comb(6, i) * ((1.09/2.09)**i) * ((1/2.09)**(6-i))

print(f'{s:.3f}')
