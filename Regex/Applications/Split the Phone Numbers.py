import re

regex_pattern = r"(?P<country>\d{1,3})[-\s](?P<local>\d{1,3})[-\s](?P<number>\d{4,10})"

n = int(input())
for _ in range(n):
    row_input = input()
    m = re.search(regex_pattern, row_input)
    output_str = (
        f"CountryCode={m.group('country')},"
        f"LocalAreaCode={m.group('local')},"
        f"Number={m.group('number')}"
    )
    print(output_str)
