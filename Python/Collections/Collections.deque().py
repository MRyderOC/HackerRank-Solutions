from collections import deque

d = deque()
N = int(input())

for i in range(N):
    ins = input().split()
    if ins[0] == 'append':
        d.append(int(ins[1]))
    if ins[0] == 'appendleft':
        d.appendleft(int(ins[1]))
    if ins[0] == 'pop':
        d.pop()
    if ins[0] == 'popleft':
        d.popleft()
        
print(' '.join(map(str, d)))
