# -*- coding: utf-8 -*-
s = input()
k = int(input())

ss = set()
for i in range(len(s)):
    for j in range(i+1,min(len(s)+1,i+k+1)):
        ss.add(s[i:j])
l = sorted(list(ss))
# print(ss)
# print(l)
print(l[k-1])
