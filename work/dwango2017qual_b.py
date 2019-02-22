# -*- coding: utf-8 -*-
t = list(input())
n = len(t)
t2 = [t[i] for i in range(n)]

for i in range(n):
    if t[i]=="?":
        if i==0:
            t[i] = "2"
        elif t[i-1]=="2":
            t[i] = "5"
        else:
            t[i] = "2"
res1 = 0
i = 0
while i<n:
    j = i
    while j<n-1 and t[j]=="2" and t[j+1]=="5":
        j += 2
    res1 = max(res1, j-i)
    i = max(i+1,j)



for i in range(n-1,-1,-1):
    if t2[i]=="?":
        if i==n-1:
            t2[i] = "5"
        elif t2[i+1]=="2":
            t2[i] = "5"
        else:
            t2[i] = "2"
res2 = 0
i = 0
while i<n:
    j = i
    while j<n-1 and t2[j]=="2" and t2[j+1]=="5":
        j += 2
    res2 = max(res2, j-i)
    i = max(i+1,j)

print(max(res1,res2))
