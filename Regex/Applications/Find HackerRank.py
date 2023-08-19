import re

start_pattern = r"^hackerrank.*"
end_pattern = r".*hackerrank$"

n = int(input())
for _ in range(n):
    row_input = input()
    start_match = re.search(start_pattern, row_input)
    end_match = re.search(end_pattern, row_input)

    if start_match and end_match:
        print(0)
    elif end_match:
        print(2)
    elif start_match:
        print(1)
    else:
        print(-1)
