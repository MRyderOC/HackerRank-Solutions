import re

s = input()
k = input()

out = []
p1 = 0
p2 = 0
while p1 < len(s):
    p2 = p1
    m = re.search(k , s[p1:])
    flag = False
    try:
        if m.start() == m.end()-1:
            flag = True
        out.append(tuple([m.start()+p2, m.end()-1+p2]))
    except:
        break
    if not flag:
        p1 = m.end() - 1 + p2
    else:
        p1 = m.end() + p2

if not out:
    print(tuple([-1, -1]))
else:
    for item in out:
        print(item)
