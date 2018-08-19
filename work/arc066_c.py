# -*- coding: utf-8 -*-
n = int(input())
d = {}
for x in input().split(" "):
    x = int(x)
    if x not in d:
        d[x] = 0
    d[x] += 1
# print(d)

if n%2==0 and 0 in d:
    print(0)
    exit()
if n%2==1 and d[0]!=1:
    print(0)
    exit()

for k,v in d.items():
    if k==0:
        continue
    if v!=2:
        print(0)
        exit()

if 0 in d:
    del d[0]
m = len(d)
MOD = 10**9 + 7

ret = 1
for _ in range(m):
    ret = (ret*2)%MOD
print(ret)
