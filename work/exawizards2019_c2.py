# -*- coding: utf-8 -*-
n,q = map(int, input().split())
s = input()
td = [input().split() for _ in range(q)]

l = 0
r = n - 1
for i in range(q-1,-1,-1):
    t,d = td[i]

    if n>l>=0:
        if s[l]==t and d=="L":
            l += 1
        elif l>0 and s[l-1]==t and d=="R":
            l -= 1

    if n>r>=0:
        if s[r]==t and d=="R":
            r -= 1
        elif r<n-1 and s[r+1]==t and d=="L":
            r += 1

print(n - l - (n-1-r))
