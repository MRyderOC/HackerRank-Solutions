import re

ip4_pattern = r"^([12]?\d?\d[.]){3}[12]?\d?\d$"
ip6_pattern = r"^([\da-f]{1,4}:){7}[\da-f]{1,4}$"

n = int(input())
for _ in range(n):
    row_input = input()
    if re.search(ip4_pattern, row_input):
        print("IPv4")
    elif re.search(ip6_pattern, row_input):
        print("IPv6")
    else:
        print("Neither")
