# -*- coding: utf-8 -*-
n,x = map(int, input().split())

if x==1 or x==2*n-1:
    print("No")
    exit()
if n==2:
    print("Yes")
    print(1)
    print(2)
    print(3)
    exit()

ret = [0 for _ in range(2*n-1)]
if x!=2:
    ret[n-1-1] = x-1
    ret[n-1] = x
    ret[n+1-1] = x+1
    ret[n+2-1] = x-2
    d = [x-2,x-1,x,x+1]
else:
    ret[n-1-1] = x+1
    ret[n-1] = x
    ret[n+1-1] = x-1
    ret[n+2-1] = x+2
    d = [x-1,x,x+1,x+2]
i = 0
j = 1
while i<2*n-1:
    if ret[i]==0:
        while j in d:
            j += 1
        ret[i] = j
        j += 1
    i += 1
print("Yes")
for x in ret:
    print(x)
