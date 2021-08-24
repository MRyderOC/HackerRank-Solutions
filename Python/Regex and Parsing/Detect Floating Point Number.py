import re


patt = re.compile(r'[-+]*\d*[.]\d+')

T = int(input())
for i in range(T):
    s = input()
    m = patt.match(s)
    if m is not None:
        try:
            float(s)
            print(True)
        except:
            print(False)
    else:
        print(False)    
