from collections import Counter


N = int(input())
arr = list(map(int, input().split()))

mean = sum(arr)/N
median = sorted(arr)[N//2] if N % 2 == 1 else (sorted(arr)[N//2] + sorted(arr)[(N//2) - 1])/2
cnt = Counter(arr)
mode = sorted([item for item in cnt.most_common() if item[1] == cnt.most_common(1)[0][1]], key=lambda x: x[0])[0][0]

print(f'{mean:.1f}')
print(f'{median:.1f}')
print(mode)
