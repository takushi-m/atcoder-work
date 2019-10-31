# -*- coding: utf-8 -*-
s = input()
n = len(s)
cnt = 1
ss = s[0]
l = 1
while l<n:
    r = l+1
    while r<n and ss==s[l:r]:
        r += 1
    if r==n and ss==s[l:r]:
        cnt -= 1

    ss = s[l:r]
    cnt += 1
    l = r

print(cnt)