# -*- coding: utf-8 -*-
s = input()
t = input()
n = len(s)

def check(idx):
    for i in range(len(t)):
        ii = idx+i
        if ii>=n:
            return False
        if s[ii]!="?" and s[ii]!=t[i]:
            return False
    return True

def restore(idx):
    res = list(s)
    for i in range(len(t)):
        ii = idx+i
        res[ii] = t[i]
    for i in range(n):
        if res[i]=="?":
            res[i] = "a"
    return "".join(res)

res = []
for i in range(n):
    if check(i):
        res.append(restore(i))
# print(res)
if len(res)==0:
    print("UNRESTORABLE")
else:
    res.sort()
    print(res[0])
