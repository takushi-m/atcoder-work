# -*- coding: utf-8 -*-
s = list(input())
n = len(s)

def calc(m):
    if m==1:
        return 2

    return m*(m+1)//2 + m*(m-1) + m

ret = 0
k = 0
for i in range(n):
    print(k,i)
    if s[i]=="D" and s[k]=="U":
        ret += calc(i-k)
        k = i
    elif s[i]=="D" and s[k]=="D":
        ret += 3
        k = i
    elif s[i]=="U" and s[k]=="D":
        k = i
print(ret)
