# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

user_input = input()
pat = r"(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])"
matches = re.findall(pat, user_input, flags=re.IGNORECASE)

if not matches:
    print(-1)
else:
    print("\n".join(matches))