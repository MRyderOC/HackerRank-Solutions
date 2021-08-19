N = int(input())
l = list(map(int, input().split()))
print(True) if (all([True if item > 0 else False for item in l]) and any([True if str(item) == str(item)[::-1] else False for item in l])) else print(False)
