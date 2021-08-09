def print_formatted(number):
    # your code goes here
    max_width = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f'{i:{max_width}} {i:{max_width}o} {i:{max_width}X} {i:{max_width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
