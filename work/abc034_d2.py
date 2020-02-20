n,k = map(int, input().split())
wpl = [list(map(int, input().split())) for _ in range(n)]

def f(w,p,x):
    p = p/100
    return p*w - w*x

def check(x):
    l = [f(wpl[i][0], wpl[i][1], x) for i in range(n)]
    l.sort(reverse=True)
    return sum(l[:k])>=0

ok = 0
ng = 1
while abs(ng-ok)>10**-7:
    mid = (ok+ng)/2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok*100)