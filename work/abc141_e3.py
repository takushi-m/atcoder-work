# -*- coding: utf-8 -*-

def Zalgo(s):
    n = len(s)
    res = [0]*n
    res[0] = n

    i = 1
    while i<n:
        j = 0
        while i+j<n and s[j]==s[i+j]:
            j += 1
        res[i] = j

        if j==0:
            i += 1
            continue

        k = 1
        while i+k<n and k+res[k]<j:
            res[i+k] = res[k]
            k += 1

        i += k
    return res

n = int(input())
s = input()

res = 0
for i in range(n):
    l = Zalgo(s[i:])
    for j in range(1,len(l)):
        res = max(res, min(l[j],j))
print(res)
