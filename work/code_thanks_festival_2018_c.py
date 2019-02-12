# -*- coding: utf-8 -*-

def f(n,xl):
    res = 0
    xl.sort()

    s = 0
    for i in range(1,n):
        s += (xl[i]-xl[i-1])*i
        res += s
    return res

def f2(n,xl):
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            res += abs(xl[i]-xl[j])
    return res

if __name__ == '__main__':
    n = int(input())
    xl = list(map(int, input().split()))
    xl.sort()
    print(f(n,xl))
