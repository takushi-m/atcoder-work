# -*- coding: utf-8 -*-
n,k = map(int, input().split())
vl = list(map(int, input().split()))

res = -1

for l in range(min(n+1,k+1)):
    for r in range(min(n+1,k+1)):
        if l+r>k or l+r>n:
            break

        w = k-(l+r)
        sl = []
        if l>0:
            sl = vl[:l]
        if r>0:
            sl += vl[-r:]
        sl = sorted(sl)
        x = w
        for i in range(min(w,len(sl))):
            if sl[i]>0:
                x = i
                break
        sl = sl[x:]
        s = sum(sl)
        res = max(res, s)

print(res)
