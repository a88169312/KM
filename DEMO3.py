#from utiity import math

"""import numpy
print(numpy.__name__, __name__)

def fib(n):
    a ,b = 0, 1
    while a < n:
        print(a , end =' ')
        a,b = b ,a+b

    print()
fib(20)
print(numpy.pi)"""

import os


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


if __name__ == '__main__':
    fib(2000)
    a, b, c, d, e = 1, 2, 3, 4, 5
    a, b, c, d, e = c, a, b, e, d
    print(a, b, c, d, e)

    a = 4
    b = 5
    print('before swap', a, b)
    # swap1
    temp = a
    a = b
    b = temp
    print('after swap', a, b)
    # swap2
    a, b = b, a
    print('after swap', a, b)

