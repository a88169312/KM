l1 = ['A', 'B', 'C']
l2 = ['A', 'B', 'C']
l3 = ['A', 'B', 'C']
l1.append('D')
l2.extend('D')
l3 += 'D'
print(l1)
print(l2)
print(l3)
l1.append(['E','F'])
l2.extend(['E','F'])
l3 += ['E','F']
print(l1)
print(l2)
print(l3)