# -*- coding: utf-8 -*-

def f(n,q,s,ql):
    g = [1]*n
    for t,d in ql:
        for i in range(n):
            if s[i]==t:
                if d=="L":
                    if i==0:
                        g[i] = 0
                    else:
                        g[i-1] += g[i]
                        g[i] = 0
                else:
                    if i==n-1:
                        g[i] = 0
                    else:
                        g[i+1] += g[i]
                        g[i] = 0
    return sum(g)

if __name__ == '__main__':
    n,q = map(int, input().split())
    s = list(input())
    ql = [input().split() for _ in range(q)]
    print(f(n,q,s,ql))
