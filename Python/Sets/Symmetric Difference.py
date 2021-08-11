# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))
out = M_set.symmetric_difference(N_set)
for item in sorted(list(out)):
    print(item)
