n,m,v,p = map(int, input().split())
al = list(map(int, input().split()))
al.sort(reverse=True)

def check(x):
    if x<p:
        return True
    if al[p-1]>al[x]+m:
        return False

    s = 0
    for i in range(n):
        if i<p-1:
            s += m
        elif p-1<=i<x:
            s += al[x]+m-al[i]
        else:
            s += m
    return s>=m*v

ok = -1
ng = n
while ng-ok>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok+1)