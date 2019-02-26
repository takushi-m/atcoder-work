# -*- coding: utf-8 -*-
num = [0,2,5,5,4,5,6,3,7,6]
#      0,1,2,3,4,5,6,7,8,9

def f(n,al):
    INF = 10**18
    dp = [-INF for _ in range(n+1)]
    dp[0] = 0

    for i in range(1,n+1):
        for a in al:
            if i-num[a]>=0:
                dp[i] = max(dp[i], dp[i-num[a]]+1)

    res = []
    al.sort(reverse=True)

    while n>0:
        for a in al:
            if n-num[a]>=0 and dp[n-num[a]]==dp[n]-1:
                res.append(str(a))
                n -= num[a]
                break

    return "".join(res)

if __name__ == '__main__':
    n,m = map(int, input().split())
    al = list(map(int, input().split()))
    print(f(n,al))

    # from random import shuffle
    # for _ in range(1000):
    #     n = 10000
    #     m = 5
    #     al = list(range(1,10))
    #     shuffle(al)
    #     al = al[:m]
    #     f(n,al)
