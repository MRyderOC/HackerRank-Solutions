# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())

flag = True
for i in range(n):
    s = set(map(int, input().split()))
    if s-A:
        flag = False
        print(flag)
        break

if flag: print(flag)
