from collections import namedtuple

N = int(input())
column_names = input().split()
student = namedtuple('student', column_names)
stds = []
for i in range(N):
    info = list(input().split())
    stds.append(student(**{c:i for c, i in zip(column_names, info)}))

sm = 0
for s in stds:
    sm += float(s.MARKS)

print(f'{sm/len(stds):.2f}')
