# -*- coding: utf-8 -*-
s = input()
i = 0
c = 0
res = 0
while i<len(s):
    j = i
    while j<len(s) and s[i]==s[j]:
        j += 1
    if s[i]=="<":
        res += (j-i)*(j-i+1)//2
        c = j-i
    else:
        res += (j-i)*(j-i+1)//2
        if c>j-i:
            res -= j-i
        else:
            res -= c

    i = j

print(res)