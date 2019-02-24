# -*- coding: utf-8 -*-
s = input()
n = len(s)
res = 0
used = [False for _ in range(n)]

while True:
    c = "5"
    idx = -1
    l = 0
    for i in range(n):
        if not used[i] and ((c=="5" and s[i]=="2") or (c=="2" and s[i]=="5")):
            used[i] = True
            c = s[i]
            idx = i
        if idx>0 and c=="5":
            l += 1

    if c=="2":
        used[idx] = False
    if l>0:
        res += 1
    else:
        break
if res==0:
    print(-1)
elif all(used):
    print(res)
else:
    print(-1)
