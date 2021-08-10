from string import ascii_lowercase

def print_rangoli(size):
    # your code goes here
    chars = ascii_lowercase[:size][::-1]
    max_width = 4 * (size-1) + 1
    other_lines = []
    for row in range(1, size):
        line_chars = chars[:row] + chars[:row][::-1][1:]
        other_lines.append('-'.join(line_chars).center(max_width,'-'))
    middle_line = '-'.join(chars[:] + chars[:][::-1][1:]).center(max_width,'-')
    
    for line in other_lines:
        print(line)
    print(middle_line)
    for line in other_lines[::-1]:
        print(line)
    
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
