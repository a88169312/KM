l1 = ['A','B','C']
t1 = ('A','B','C')
print(hex(id(l1)))
print(hex(id(t1)))
l1 += ['D']
t1 += ('D',)
print(hex(id(l1)))
print(hex(id(t1)))
print(l1)
print(t1)
sales = {'iphone':500,'ipad':300}
#print(sales.items())
for (k,v) in sales.items():
    print(f'{k},{v}')