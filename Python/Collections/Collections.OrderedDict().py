from collections import OrderedDict

N = int(input())

dic = OrderedDict()
for i in range(N):
    ins = input().split()
    price = ins[-1]
    item = ' '.join(ins[:-1])
    if item not in dic:
        dic[item] = int(price)
    else:
        dic[item] += int(price)

for item in dic:
    print(f'{item} {dic[item]}')
