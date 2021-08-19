cube = lambda x: x ** 3 

def fibonacci(n):
    l = []
    for i in range(n):
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(l[i-1] + l[i-2])
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
