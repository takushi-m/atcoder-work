p = float(input())

# f = x + p*2^(-x/1.5)
def f(x):
    return x + p*2**(-x/1.5)

x0 = 0.0
x3 = p

while abs(x3-x0)>10**-8:
    x1 = (x3-x0)/3.0 + x0
    x2 = (x3-x0)*2.0/3.0 + x0
    f1 = f(x1)
    f2 = f(x2)
    if f1<f2:
        x3 = x2
    else:
        x0 = x1

print(f(x0))