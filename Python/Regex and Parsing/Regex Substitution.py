# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pat_and = r"(?<= )&&(?= )"
pat_or = r"(?<= )\|\|(?= )"
n = int(input())

for _ in range(n):
    print(re.sub(
        pat_and, "and", re.sub(pat_or, "or", input())
    ))