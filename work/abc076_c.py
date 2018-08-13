# -*- coding: utf-8 -*-

s = input()
t = input()

def isMatch(idx):
    si = idx
    ti = 0
    while si<len(s) and ti<len(t):
        if s[si]==t[ti]:
            si += 1
            ti += 1
            continue
        if s[si]=="?":
            si += 1
            ti += 1
            continue
        if s[si]!=t[ti]:
            return False
    return ti==len(t)

ret = None
for i in range(len(s)-1,-1,-1):
    if isMatch(i):
        ret = s[:i]+t+s[i+len(t):]
        break

if ret is None:
    print("UNRESTORABLE")
else:
    print(ret.replace("?", "a"))
