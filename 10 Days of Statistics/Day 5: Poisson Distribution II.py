mean_A, mean_B = list(map(float, input().split()))

C_A = round(160 + 40 * mean_A * (1+mean_A), 3)
C_B = round(128 + 40 * mean_B * (1+mean_B), 3)

print(f'{C_A:.3f}\n{C_B:.3f}')
