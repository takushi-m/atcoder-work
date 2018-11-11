# -*- coding: utf-8 -*-
n,k = map(int, input().split())
xyc = []
for _ in range(n):
    x,y,c = input().split()
    x = int(x)
    y = int(y)
    xyc.append((x%(2*k), y%(2*k), c))


res = 0
for xk in range(k+1):
    for yk in range(k+1):
        for ck in ["B", "W"]:
            tmp = 0
            for i in range(n):
                x,y,c = xyc[i]
                x = (x-xk+2*k)%(2*k)
                y = (y-yk+2*k)%(2*k)
                # print(x,y,c)
                if c==ck:
                    if k>x>=0 and k>y>=0:
                        tmp += 1
                    elif 2*k>x>=k and 2*k>y>=k:
                        tmp += 1
                else:
                    if k>x>=0 and 2*k>y>=k:
                        tmp += 1
                    elif 2*k>x>=k and k>y>=0:
                        tmp += 1
            # print(xk,yk,ck,tmp)
            res = max(res, tmp)
print(res)
