# -*- coding: utf-8 -*-


def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def f(n,k,al):
    if k==1:
        return n*(n-1)//2

    kl = []
    r = 1
    while r*r<=k:
        if k%r==0:
            kl.append(r)
            kl.append(k//r)
        r += 1
    kl = list(set(kl))
    kl.sort()
    # print(kl)
    d = {}
    for a in al:
        x = gcd(a,k)
        if x not in d:
            d[x] = 0
        d[x] += 1
    # print(d)
    res = 0
    for i in range(len(kl)):
        for j in range(i,len(kl)):
            k1 = kl[i]
            k2 = kl[j]
            if gcd(k1*k2,k)!=k:
                continue
            if k1 in d and k2 in d:
                # print(k1,k2)
                if k1!=k2:
                    res += d[k1]*d[k2]
                else:
                    res += d[k1]*(d[k1]-1)//2

    return res

def f2(n,k,al):
    from itertools import combinations
    res = 0
    for p in combinations(al,2):
        if p[0]*p[1]%k==0:
            res += 1
    return res

if __name__ == '__main__':
    n,k = map(int, input().split())
    al = list(map(int, input().split()))
    print(f(n,k,al))
    # print("f2",f2(n,k,al))

    # from random import randint
    # n = 10
    #
    # for _ in range(100):
    #     k = randint(1,100)
    #     al = [randint(1,30) for _ in range(n)]
    #
    #     a1 = f(n,k,al)
    #     a2 = f2(n,k,al)
    #     if a1!=a2:
    #         print(a1,a2)
    #         print(n,k,al)
