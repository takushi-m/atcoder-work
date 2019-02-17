# -*- coding: utf-8 -*-
n = int(input())
s = list(input())

idx = -1
max_cnt = 0
max_idx = -1
while idx<n-1:
    idx += 1
    if s[idx]=="-":
        continue
    cnt = 0
    i = idx
    while s[idx]==">":
        cnt += 1
        idx += 1
    if max_cnt<cnt:
        max_cnt = cnt
        max_idx = i

if max_idx>0:
    s[max_idx-1] = ">"
elif max_idx<n-1:
    s[max_idx+max_cnt] = ">"

res = 0.0
k = 0
for i in range(n):
    if s[i] == "-":
        res += 1.0
    else:
        if s[i-1]==">":
            k += 1
        else:
            k = 0
        res += 1/(k+2)

print("{:.10}".format(res))
