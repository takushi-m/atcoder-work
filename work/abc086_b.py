from math import sqrt

a,b = input().split()

x = int(a+b)
if x==int(sqrt(x))**2:
    print("Yes")
else:
    print("No")