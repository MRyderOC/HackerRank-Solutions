def minion_game(s):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0    
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i
            
    if kevin < stuart:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
