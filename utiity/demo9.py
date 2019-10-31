a1 = 5
a2 = 5.0
a3 = '5'
print(type(a1), type(a2), type(a3))
a4 = int(a3)
a5 = float(a3)
print(type(a4), a4)
print(type(a5), a5)
a6 = 3.14159
a7 = int(a6)
a8 = float(a6)
print(type(a7), a7)
print(type(a8), a8)
# now start with complex number
a9 = '5+3j'
a10 = complex(a9)
print(type(a9), type(a10))
print(a10.real, a10.imag)
print(a10.conjugate)
a11 = 1
a12 = complex(a11)
print(type(a12), a12)
a13 = -1
a14 = (-1)**0.5
print(type(a14), a14)
#complex arithmatic
a15 = a10.conjugate()
print(abs(a15), abs(a10))