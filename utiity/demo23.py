l1 = ['Apple', 'Banana', 'Citron', 'Donut']
print('Apple' in l1, 'Apple' not in l1)
print('Elephant' in l1, 'Elephant' not in l1)

for l in l1:
    print(len(l), l)
x1, x2, x3, x4 = l1
print(x1, x3,end='\n\n')
print(x2, x4)
print(l1.index('Apple'), l1.index('Donut'))
print('Apple' in l1)
print(l1.index('Apple'))