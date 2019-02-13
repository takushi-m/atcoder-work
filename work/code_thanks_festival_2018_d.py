# -*- coding: utf-8 -*-
s = input()
res = 1
c = s[0]
for i in range(1,len(s)):
    if s[i]>c:
        continue
    else:
        c = s[i]
        res += 1
print(res)
