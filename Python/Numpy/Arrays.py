import numpy

def arrays(arr):
    return numpy.flip(list(map(float, arr)))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
