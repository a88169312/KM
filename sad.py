import sys
import os
import DEMO3

DEMO3.fib(300)


if __name__=='__main__':
    DEMO3.fib(int(sys.argv[1]))
print(sys.path)
print(type(sys.path))

print(os.system("COLOR fc"))

sad = os.system("pip list --format=json")
print(sad)