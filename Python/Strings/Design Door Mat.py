# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = list(map(int,(input().split())))

if N % 2 != 1 or M/N != 3.0:
    pass

size = (N-1)//2

other_lines = []
for i in range(size):
    num = 2 * i + 1
    mid_pat = '.|.' * num
    other_lines.append(mid_pat.center(M,'-'))
    
middle_line = 'WELCOME'.center(M, '-')

for line in other_lines:
    print(line)
print(middle_line)
for line in other_lines[::-1]:
    print(line)
    
