# -*- coding: utf-8 -*-
s = input()
n = len(s)

for i in range(n-1):
    if s[i]==s[i+1]:
        print(i+1,i+2)
        exit()

for i in range(n-2):
    if s[i]==s[i+1] or s[i+1]==s[i+2] or s[i]==s[i+2]:
        print(i+1, i+3)
        exit()

print(-1,-1)
