l1 = ['iphoneXS', 'iphone11', 'ipadPro', 'applewatch4',
      'airpodPro']

items = ['iphoneXS', 'galaxy', 'htc', 'ipadPro',
         'applewatch4', 'iphone9']
#x1 = 'iphoneXS'
#print(x1 in l1)
#print(l1.index(x1))
for i in items:
    print(i in l1 and l1.index(i))

print('type1', True and True)
print('type2', True and False)
print('type2', True and 3.14)
print('type2', True and 'hello world')
print('type2', True and [1, 3, 5])
print('0r_type1', False or True)
print('0r_type2', False or False)
print('0r_type3', False or 100)
print('0r_type4', False or [1,3,5])
print('0r_type5', False or 'hello world')
print('0r_type6', False or None)