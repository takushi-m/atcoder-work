# -*- coding: utf-8 -*-
s = input()
sn = len(s)
t = input()
tn = len(t)

ss = ""
for i in range(sn-tn+1):
    match = True
    for j in range(tn):
        if s[i+j]=="?" or s[i+j]==t[j]:
            pass
        else:
            match = False
            break
    if match:
        ss = s[:i] + t + s[i+tn:]

if ss=="":
    print("UNRESTORABLE")
    exit()

print(ss.replace("?","a"))