from decimal import Decimal as Dec
from decimal import ROUND_HALF_UP,\
     ROUND_HALF_DOWN, ROUND_HALF_EVEN

digits = [Dec(1), Dec('0.1'), Dec('0.01'),
          Dec('0.001')]

x1 = Dec(1/6)
print(x1)
x2 = Dec(0.5)
print(x2)
x3 = Dec(0.4)
print(x3)
rounds = [ROUND_HALF_UP,ROUND_HALF_DOWN, ROUND_HALF_EVEN]
for r in rounds:
    x4 = Dec(1.5)
    print(type(x4), x4)
    y4 = x4.quantize(Dec(1), ROUND_HALF_UP)
    print(y4)
    x5 = Dec(2.5)
    print(type(x5), x5)