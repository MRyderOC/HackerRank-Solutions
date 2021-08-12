# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for test_case in range(T):
    n_A = int(input())
    A = set(map(int, input().split()))
    n_B = int(input())
    B = set(map(int, input().split()))
    if A-B:
        print(False)
    else:
        print(True)
    
