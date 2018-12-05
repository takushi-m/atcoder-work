# -*- coding: utf-8 -*-
from math import factorial as fact
def comb(n,r):
    return fact(n) // (fact(r)*fact(n-r))

n,a,b = map(int, input().split())
vl = list(map(int, input().split()))
vl.sort(reverse=True)

res_avg = sum(vl[:a])/a
res_cnt = 0
last_v = vl[a-1]

cnt_all = 0
for v in vl:
    if v==last_v:
        cnt_all += 1

for m in range(a,b+1):
    if sum(vl[:m])/m == res_avg:
        cnt_in = 0
        for i in range(m):
            if last_v==vl[i]:
                cnt_in += 1
        res_cnt += comb(cnt_all, cnt_in)

print("{:6f}".format(res_avg))
print(res_cnt)
