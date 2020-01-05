# -*- coding: utf-8 -*-
n = int(input())
al = list(map(int, input().split()))

cnt = 0
s = 1
for a in al:
    if a==s:
        s += 1
    else:
        cnt += 1

if cnt==n:
    print(-1)
else:
    print(cnt)