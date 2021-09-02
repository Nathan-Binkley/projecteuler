import math


cap = 1001

for a in range(1, cap):
    for b in range(a+1, cap):
        c = math.sqrt(a**2+b**2)
        if c + a + b == 1000:
            print(a,b,c)
            print("sol",a*b*c)
        