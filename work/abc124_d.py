# -*- coding: utf-8 -*-

def check(l,r,k,s,acc):
    cnt = acc[r] - acc[l]
    if l>0 and s[l]=="0":
        cnt += 1
    return cnt<=k

def f(n,k,s):
    acc = [0]*(n+1)
    for i in range(n):
        if i==0:
            if s[i]=="0":
                acc[i+1] = 1
        else:
            if s[i]=="0" and s[i-1]=="1":
                acc[i+1] = acc[i]+1
            else:
                acc[i+1] = acc[i]

    left = 0
    right = 0
    res = -1
    while left<n:
        while right<n and check(left,right+1,k,s,acc):
            right += 1

        res = max(res, right-left)

        if left==right:
            right += 1

        left += 1

    return res

if __name__ == '__main__':
    n,k = map(int, input().split())
    s = input()
    print(f(n,k,s))
