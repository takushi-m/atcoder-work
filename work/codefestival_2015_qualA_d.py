n,m = map(int, input().split())
xl = [int(input()) for _ in range(m)]

def check(t):
    left = 1
    for x in xl:
        if x-left>t:
            return False
        if left>=x:
            left = x + t + 1
        else:
            dx = x - left
            r1 = x + t - dx*2
            r2 = x + (t - dx)//2
            left = max(r1, r2) + 1
    return left>n

ok = n*2
ng = -1
while (ok-ng)>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)