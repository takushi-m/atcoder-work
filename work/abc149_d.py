# -*- coding: utf-8 -*-
n,k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()

l = [""]*k
for i in range(n):
    l[i%k] += t[i]

res = 0
for x in l:
    prev = ""
    score = 0
    for i in range(len(x)):
        if x[i]=="r":
            if prev!="p":
                score += p
                prev = "p"
            else:
                prev = ""
        elif x[i]=="s":
            if prev!="r":
                score += r
                prev = "r"
            else:
                prev = ""
        else:
            if prev!="s":
                score += s
                prev = "s"
            else:
                prev = ""
    res += score

print(res)