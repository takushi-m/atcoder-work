# -*- coding: utf-8 -*-
M,D = map(int, input().split())

def check(m,d):
    d1 = d%10
    d2 = d//10
    return d1>=2 and d2>=2 and d1*d2==m

res = 0
for m in range(1,M+1):
    for d in range(1,D+1):
        if check(m,d):
            res += 1

print(res)
