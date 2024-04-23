# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(n):
    if n == 1:
        print("Not prime")
        return
    if n == 2:
        print("Prime")
        return

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Not prime")
            return

    print("Prime")


t = int(input())
for _ in range(t):
    is_prime(int(input()))
