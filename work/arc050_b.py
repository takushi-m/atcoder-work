r,b = map(int, input().split())
x,y = map(int, input().split())

def check(n):
    return r>=n and b>=n and (r-n)//(x-1) + (b-n)//(y-1) >= n


ok = -1
ng = 10**18
while ng-ok>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)