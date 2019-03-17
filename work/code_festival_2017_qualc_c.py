# -*- coding: utf-8 -*-
s = input()
rs = "".join(reversed(s))
n = len(s)

res = 0
i = 0
j = 0
while i+j<n:
    if s[i]==rs[j]:
        i += 1
        j += 1
    elif s[i]=="x":
        res += 1
        i += 1
    elif rs[j]=="x":
        res += 1
        j += 1
    else:
        print(-1)
        exit()

print(res)
