# -*- coding: utf-8 -*-
n,m = map(int, input().split())
xl = list(map(int, input().split()))

if n>=m:
    print(0)
    exit()
if n==1:
    print(max(xl)-min(xl))
    exit()


xl.sort()
l = []
for i in range(m-1):
    l.append(xl[i+1]-xl[i])
l.sort(reverse=True)

res = sum(l) - sum(l[0:n-1])
print(res)
