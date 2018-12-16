# -*- coding: utf-8 -*-
h,w = map(int, input().split())
inf = 10**6
field = []
d = []
res = 0
for _ in range(h):
    line = list(input())
    field.append(line)
    d.append([inf]*w)
    for s in line:
        if s==".":
            res += 1

d[0][0] = 0
diff = [
    [1,0]
    ,[0,1]
    ,[-1,0]
    ,[0,-1]
]

flag = True
while flag:
    flag = False
    for hi in range(h):
        for wi in range(w):
            if d[hi][wi]<inf:
                for (dh,dw) in diff:
                    if h>hi+dh>=0 and w>wi+dw>=0 and field[hi+dh][wi+dw]=="." and d[hi+dh][wi+dw]>d[hi][wi]+1:
                        d[hi+dh][wi+dw] = d[hi][wi]+1
                        flag = True

if d[h-1][w-1]<inf:
    print(res-d[h-1][w-1]-1)
else:
    print(-1)
