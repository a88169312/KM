import utiity

def fib(n):
    print(utiity.package_global_variable)
    a,b = 0,1
    while a < n :
        print(a , end='')
        a ,b = b ,a+b
    print()