# -*- coding: utf-8 -*-
from pprint import pprint
def f(n,m,edge):
    d = {}
    for a,b,l in edge:
        if l not in d:
            d[l] = {}

        if a not in d[l]:
            d[l][a] = []
        d[l][a].append(b)

        if b not in d[l]:
            d[l][b] = []
        d[l][b].append(a)

    for l in d.keys():
        for x in d[l].keys():
            d[l][x].sort()


    def lower_bound(al, key):
        """
        一般に左側が満たしておらず、右側は満たしている判定基準(境目は一つ)ならlower_boundになる
        (条件を満たすもののうち、最小のインデックスを返す)
        単調にさえなっていれば、左右が逆になっていても検索には使える(ng/okも一緒に逆にする必要がある)
        """
        def isOk(a):
            # alの中でkey以上のアイテムのうち最小のインデックスを返す
            # upper_boundにする時にはa>key
            return a>key

        ng = -1
        ok = len(al)

        while abs(ok-ng)>1:
            mid = (ok+ng)//2

            if isOk(al[mid]):
                ok = mid
            else:
                ng = mid

        return ok

    res = 0
    for a,b,l in edge:
        r = 2540-l
        if r not in d:
            continue
        if b in d[r]:
            res += len(d[r][b]) - lower_bound(d[r][b], a)
        if a in d[r]:
            res += len(d[r][a]) - lower_bound(d[r][a], b)
    return res

def f2(n,m,edge):
    path = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for a,b,l in edge:
        path[a][b] = l
        path[b][a] = l

    res = []
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(a+1,n+1):
                if path[a][b]>0 and path[b][c]>0 and path[a][b]+path[b][c]==2540:
                    res.append((a,b,c))
    return res

if __name__ == '__main__':
    n,m = map(int, input().split())
    edge = []
    for _ in range(m):
        a,b,l = map(int, input().split())
        edge.append((a,b,l))
    print(f(n,m,edge))
    # n = 5
    # m = 4
    # edge = [(2, 5, 1246), (1, 5, 1343), (3, 4, 1036), (1, 3, 1197)]
    # # 3-1-5
    # res1 = f(n,m,edge)
    # res2 = f2(n,m,edge)
    # print(res1,res2)
