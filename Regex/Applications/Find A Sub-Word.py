import re

subword_pattern = lambda subword: fr"\w+{subword}\w+"

n = int(input())
whole_doc = "\n".join([input() for _ in range(n)])

queries = int(input())
for _ in range(queries):
    sub_word = input()
    print(len(re.findall(subword_pattern(sub_word), whole_doc)))
