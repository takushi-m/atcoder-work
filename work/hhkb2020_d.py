mod = 10**9+7

t = int(input())
nab = [list(map(int, input().split())) for _ in range(t)]

for n,a,b in nab:
    if a+b>n:
        x4 = 0
    else:
        x4 = (n-a-b+2)*(n-a-b+1)//2
    x4 %= mod
    
    x3 = 2*x4
    x3 %= mod

    x2 = (n-a+1)*(n-b+1) + mod - x3
    x2 %= mod

    x1 = x2*x2
    x1 %= mod

    r = pow(n-a+1,2,mod)*pow(n-b+1,2,mod) + mod - x1
    r %= mod

    print(r)
