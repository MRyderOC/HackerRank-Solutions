if __name__ == '__main__':
    s = input()
    alphaNum, alphabet, digit, lower, upper = False, False, False, False, False
    for char in s:
        if char.isalnum():
            alphaNum = True
        if char.isalpha():
            alphabet = True
        if char.isdigit():
            digit = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
    
    print(alphaNum)
    print(alphabet)
    print(digit)
    print(lower)
    print(upper)
