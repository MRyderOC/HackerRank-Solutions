import re

def isValidUID(s: str):
    upper = re.search(r'([A-Z].*){2}', s)
    digits = re.search(r'(\d.*){3}', s)
    alpha_10char = re.match(r'[a-zA-Z0-9]{10}$', s)
    no_repeating = len(set(s)) == len(s)
    
    return True if all([upper, digits, alpha_10char, no_repeating]) else False


for _ in range(int(input())):
    s = input()
    print('Valid') if isValidUID(s) else print('Invalid')
