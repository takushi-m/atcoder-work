# -*- coding: utf-8 -*-
from string import ascii_lowercase

def lower_bound(al, key):
    """
    一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
    (条件を満たすもののうち、最小のインデックスを返す)
    単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
    """
    def isOk(a):
        # alの中でkey以上のアイテムのうち最小のインデックスを返す
        # upper_boundにする時にはa>key
        return a>=key

    ng = -1
    ok = len(al)
    if ok==0:
        return -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2

        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid
    return ok


def f(s,t):
    n = len(s)
    s += s

    d = {}
    for c in ascii_lowercase:
        d[c] = []

    for i in range(2*n):
        d[s[i]].append(i)


    m = len(t)
    idx = 0
    for i in range(m):
        c = lower_bound(d[t[i]],idx%n)
        if c>=0:
            idx += d[t[i]][c] - idx%n
        else:
            return -1

    return idx+1

if __name__ == '__main__':
    s = input()
    t = input()
    print(f(s,t))
