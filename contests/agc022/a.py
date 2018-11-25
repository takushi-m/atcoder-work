# -*- coding: utf-8 -*-

alp = "abcdefghijklmnopqrstuvwxyz"

s = list(input())
ss = set(s)

if len(s)<26:
    for x in list(alp):
        if x not in ss:
            print("".join(s)+x)
            exit()

idx = 0
for (i,x) in enumerate(s):
    if i>1 and s[i-2]<s[i-1] and s[i-1]>s[i]:
        l = list(filter(lambda x:x>s[i-2], s[i-1:]))
        if len(l)==0:
            l.appebd(s[i])
        y = min(l)
        print("".join(s[0:i-2])+y)
        exit()
    elif i>1 and s[i-2]>s[i-1] and s[i-1]<s[i]:
        l = list(filter(lambda x:x>s[i], s[i-1:]))
        if len(l)==0:
            l.append(s[i])
        y = min(l)
        print("".join(s[0:i])+y)
        exit()


print("-1")
