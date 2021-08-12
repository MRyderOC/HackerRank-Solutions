# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
s = list(map(int, input().split()))

# Find every rooms occurences and store them in a dictionary
dic = {room:0 for room in set(s)}
for room in s:
    dic[room] += 1

# Reverse the dictioanry's keys and values and just keep the Capitan's room
dic2 = {v:k for k, v in dic.items() if v != K}
print(dic2[1])
