p = float(input())

def f(x):
    return x + p*pow(2.0, -x/1.5)

l = 0
r = p

while r-l>10**-10:
    m1 = l + (r-l)/3
    m2 = l + (r-l)*2/3

    if f(m1)>f(m2):
        l = m1
    else:
        r = m2

print(f(r))
