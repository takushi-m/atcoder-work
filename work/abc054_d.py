# -*- coding: utf-8 -*-
inf = 10**10
n,ma,mb = map(int, input().split())

a = []
b = []
c = []
for _ in range(n):
    x,y,z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

memo = {}
def rec(i, maj, mbj):
    k = str(i)+"-"+str(maj)+"-"+str(mbj)
    if k in memo:
        return memo[k]
    # print(i, ":", maj, mbj, maj/ma, mbj/mb)
    ret = 0
    if i==n:
        if maj>0 and mbj>0 and maj/ma == mbj/mb:
            ret = 0
        else:
            ret = inf
    elif maj>0 and mbj>0 and maj/ma == mbj/mb:
        ret = 0
    else:
        r1 = rec(i+1, maj, mbj) # i番目を使わない場合
        # i番目を使う場合
        r2 = rec(i+1, maj+a[i], mbj+b[i]) + c[i]
        if r1>0 and r2==0:
            ret = r1
        elif r1==0 and r2>0:
            ret = r2
        else:
            ret = min(r1,r2)
    memo[k] = ret
    return ret

ret = rec(0, 0, 0)
if ret == inf:
    print(-1)
else:
    print(ret)
