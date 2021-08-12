# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))

N = int(input())
for operation in range(N):
    cmd = input().split()
    s = set(map(int, input().split()))
    if cmd[0].startswith('intersection'):
        A &= s
    elif cmd[0].startswith('update'):
        A |= s
    elif cmd[0].startswith('symmetric'):
        A ^= s
    elif cmd[0].startswith('difference'):
        A -= s

print(sum(A))
    
