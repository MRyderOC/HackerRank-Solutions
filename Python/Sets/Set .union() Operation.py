# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n_list = set(map(int, input().split()))
b = int(input())
b_list = set(map(int, input().split()))

print(len(n_list.union(b_list)))
