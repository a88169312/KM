l1 = [1, 3, 5, 7, 9]

l2 = ['hello', 300, 3.14, None, (1, 2, 3)]
print(type(l1), type(l2))
l3 = list('A','B','c')
l4 = list('ABC')
l5 = list('ABC')
print(type(l3), type(l4))
print(l3,l4)
print(hex(id(l3)), hex(id(l4)),hex(id(l5)))