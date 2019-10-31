l1 = [1, 3, 5, 7, 9]
l2 = l1
print(l1, l2)
print(l1 == l2, hex(id(l1)), hex(id(l2)))
l3 = l1[:]
print(l3, l1 == l3, l2 == l3)
print(hex(id(l3)))
l4 = list(l1)
print(l4, l1 == l4, l2 == l4, l3 == l4)
print(hex(id(l4)))