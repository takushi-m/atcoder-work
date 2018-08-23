# -*- coding: utf-8 -*-
n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()
a = sum(s)

if a%10!=0:
    print(a)
    exit()

for i in range(n):
    if s[i]%10==0:
        continue
    a -= s[i]
    if a%10!=0:
        print(a)
        exit()

print(0)
