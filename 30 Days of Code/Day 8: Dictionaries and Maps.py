# Enter your code here. Read input from STDIN. Print output to STDOUT
m = {}
n = int(input())
for _ in range(n):
    name, phone_number = input().split(" ")
    m[name] = phone_number

while True:
    try:
        q = input()
    except Exception:
        break

    num = m.get(q)
    if num:
        print(f"{q}={num}")
    else:
        print("Not found")
