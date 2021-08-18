import re
T = int(input())

for i in range(T):
    r = input()
    try:
        re.compile(r)
        print(True)
    except:
        print(False)
