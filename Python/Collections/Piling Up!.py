from collections import deque

for i in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    
    top = max(blocks[0], blocks[-1])
    flag = True
    i = 0
    while i < n:
        left, right = blocks[0], blocks[-1]
        m = max(left, right)
        if left == right:
            tmp = blocks.popleft()
            if len(blocks) != 0:
                blocks.pop()
                i += 1
        elif m == left:
            tmp = blocks.popleft()
        elif m == right:
            tmp = blocks.pop()
        i += 1
        if tmp > top:
            flag = False
            break
        else:
            top = tmp
    
    if not flag:
        print('No')
    else:
        if len(blocks) == 0:
            print('Yes')
    
