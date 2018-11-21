# -*- coding: utf-8 -*-
a,b,c = map(int, input().split())

res = 0
s = set((a,b,c))
while True:
    if a%2==1 or b%2==1 or c%2==1:
        break
    res += 1
    a,b,c = b//2+c//2,a//2+c//2,a//2+b//2

    if (a,b,c) in s:
        # print(s,a,b,c)
        print(-1)
        exit()
    s.add((a,b,c))
print(res)
