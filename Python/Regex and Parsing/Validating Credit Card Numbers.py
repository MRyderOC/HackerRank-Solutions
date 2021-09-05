import re

p1 = r'^[4-6]\d{3}(-\d{4}){3}$'
p2 = r'^[4-6]\d{15}$'
p3 = r'(\d)\1{3,}'

for i in range(int(input())):
    s = input()
    m1 = re.match(p1, s)
    m2 = re.match(p2, s)
    m3 = re.search(p3, s.replace('-', ''))
    
    print('Valid' if (m1 or m2) and not m3 else 'Invalid')
    
