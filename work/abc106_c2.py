# -*- coding: utf-8 -*-
s = input()
k = int(input())

if len(s)==1:
    print(s[0])
elif k==1:
    print(s[0])
else:
    cnt = 0
    idx = 0
    for c in list(s):
        idx += 1
        if c=="1":
            cnt += 1
        else:
            break
    if k<=cnt:
        print(1)
    else:
        print(s[idx-1])
