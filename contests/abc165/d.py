from math import floor

def f(a,b,x):
    return floor(a*x/b) - a*floor(x/b)

a,b,n = map(int, input().split())
res = -10**9
for x in range(max(min(n,b)-100,0),min(n,b)+1):
    res = max(res, f(a,b,x))
print(res)