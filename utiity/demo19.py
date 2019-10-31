import numpy

a1 = numpy.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
a2 = a1
a3 = a1.copy
print(a1, a2, a3)
a1 *= 2
print(a1, a2, a3)