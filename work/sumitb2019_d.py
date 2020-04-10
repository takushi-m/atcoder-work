n = int(input())
s = list(input())

d = [[] for _ in range(10)]
for i in range(n):
    d[int(s[i])].append(i)

def lower_bound(al,k):
    if len(al)==0:
        return -1
    ng = -1
    ok = len(al)
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if al[mid]>k:
            ok = mid
        else:
            ng = mid
    if ok==len(al):
        return -1
    return ok

def check(pl):
    pos = -1
    res = []
    for i in range(3):
        pos = lower_bound(d[pl[i]], pos)
        if pos<0:
            return False
        pos = d[pl[i]][pos]
        res.append(pos)
    return True

res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if check([i,j,k]):
                res += 1

print(res)