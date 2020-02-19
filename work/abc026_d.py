from math import sin,pi

a,b,c = map(int, input().split())

def f(t):
    return a*t + b*sin(c*t*pi)

lo = 0
hi = 1000
while abs(f(hi)-f(lo))>10**-7:
    mid = (hi+lo)/2
    x = f(mid)
    if x>100:
        hi = mid
    else:
        lo = mid

print(hi)
