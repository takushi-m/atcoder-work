n = int(input())
hs = [list(map(int, input().split())) for _ in range(n)]

def check(x):
    l = [(x-hs[i][0])/hs[i][1] for i in range(n)]
    l.sort()
    for i in range(n):
        if l[i]<i:
            return False
    return True

ng = -1
ok = 10**15
while ok-ng>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)