import re
from email.utils import parseaddr, formataddr

for _ in range(int(input())):
    name, email = parseaddr(input())
    if re.match(r'([a-zA-Z]+[a-zA-Z1-9._-]*)[@]([a-zA-Z]+)[.]([a-zA-Z]{1,3})$', email):
        print(formataddr((name, email)))
    
