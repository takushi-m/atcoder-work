# -*- coding: utf-8 -*-
n = int(input())
c = []
s = []
f = []

for _ in range(n-1):
    line = input().split(" ")
    c.append(int(line[0]))
    s.append(int(line[1]))
    f.append(int(line[2]))

def calc(idx, t):
    # print(idx,t)
    ret = 0
    if idx==n-1:
        return t

    if t<s[idx]:
        t = s[idx]

    if t%f[idx]==0:
        return calc(idx+1, t+c[idx])
    else:
        return calc(idx+1, (t//f[idx]+1)*f[idx]+c[idx])


for i in range(n):
    # print("--",i,"--")
    print(calc(i, 0))
