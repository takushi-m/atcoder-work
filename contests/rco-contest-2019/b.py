# -*- coding: utf-8 -*-
from random import randint
from copy import deepcopy
class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return

        if x<y:
            self.par[y] = x
        else:
            self.par[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

uf = UnionFind(n*n)
res = []
for hi in range(n):
    for wi in range(n):
        if a[hi][wi]==8:
            cnt = 0
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                if n>hi+d[0]>=0 and n>wi+d[1]>=0:
                    if a[hi+d[0]][wi+d[1]] in (6,7,8,9):
                        cnt += 1
            if cnt>0:
                res.append((1,hi,wi))
                a[hi][wi] = 9
        elif a[hi][wi]==7:
            cnt = 0
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                if n>hi+d[0]>=0 and n>wi+d[1]>=0:
                    if a[hi+d[0]][wi+d[1]] in (6,7,8,9):
                        cnt += 1
            if cnt>0:
                res.append((1,hi,wi))
                res.append((1,hi,wi))
                a[hi][wi] = 9
        elif a[hi][wi]==6:
            cnt = 0
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                if n>hi+d[0]>=0 and n>wi+d[1]>=0:
                    if a[hi+d[0]][wi+d[1]] in (6,7,8,9):
                        cnt += 1
            if cnt>1:
                res.append((1,hi,wi))
                res.append((1,hi,wi))
                res.append((1,hi,wi))
                a[hi][wi] = 9
        # elif a[hi][wi]==5:
        #     cnt = 0
        #     for d in [[0,1],[1,0],[0,-1],[-1,0]]:
        #         if n>hi+d[0]>=0 and n>wi+d[1]>=0:
        #             if a[hi+d[0]][wi+d[1]] in (6,7,8,9):
        #                 cnt += 1
        #     if cnt>0:
        #         res.append((1,hi,wi))
        #         res.append((1,hi,wi))
        #         res.append((1,hi,wi))
        #         res.append((1,hi,wi))
        #         a[hi][wi] = 9

used = [[False for _ in range(n)] for _ in range(n)]
def dfs(hi,wi):
    if used[hi][wi]:
        return

    st = [(hi,wi)]
    while len(st)>0:
        hj,wj = st.pop()
        used[hj][wj] = True
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            if n>hj+d[0]>=0 and n>wj+d[1]>=0 and not used[hj+d[0]][wj+d[1]]:
                if a[hi][wi]==a[hj+d[0]][wj+d[1]]:
                    st.append((hj+d[0], wj+d[1]))

def dfscnt(hi,wi):
    if used[hi][wi]:
        return 0
    res = 1
    used2 = set()
    st = [(hi,wi)]
    used2.add((hi,wi))
    while len(st)>0:
        hj,wj = st.pop()
        used2.add((hj,wj))
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            if n>hj+d[0]>=0 and n>wj+d[1]>=0 and (hj+d[0],wj+d[1]) not in used2:
                if a[hi][wi]==a[hj+d[0]][wj+d[1]]:
                    st.append((hj+d[0], wj+d[1]))
                    res += 1
    return res

for hi in range(n):
    for wi in range(n):
        cnt = 0
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            if n>hi+d[0]>=0 and n>wi+d[1]>=0:
                if a[hi][wi]==9 and a[hi+d[0]][wi+d[1]]==9:
                    uf.unite(n*hi+wi, n*(hi+d[0])+wi+d[1])

for hi in range(n):
    for wi in range(n):
        if a[hi][wi]<4:
            continue
        t = []
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            if n>hi+d[0]>=0 and n>wi+d[1]>=0:
                if a[hi+d[0]][wi+d[1]]==9:
                    t.append((hi+d[0],wi+d[1]))
        if len(t)<2:
            continue
        cnt = 0
        for i in range(len(t)-1):
            hj = t[i][0]
            wj = t[i][1]
            hj2 = t[i+1][0]
            wj2 = t[i+1][1]
            if not uf.same(hj*n+wj, hj2*n+wj2):
                cnt += 1
        if cnt>0:
            for _ in range(9-a[hi][wi]):
                res.append((1,hi,wi))
            a[hi][wi] = 9
            for i in range(len(t)-1):
                hj = t[i][0]
                wj = t[i][1]
                hj2 = t[i+1][0]
                wj2 = t[i+1][1]
                uf.unite(hj*n+wj, hj2*n+wj2)

for hi in range(n):
    for wi in range(n):
        if len(res)>=m:
            continue
        if a[hi][wi]==9 and dfscnt(hi,wi)>=9:
            res.append((2,hi,wi))
            dfs(hi,wi)

update = True
while len(res)<m-1 and update:
    update = False
    for hi in range(n):
        for wi in range(n):
            if len(res)<m-1 and not used[hi][wi] and dfscnt(hi,wi)>=a[hi][wi]:
                res.append((2,hi,wi))
                dfs(hi,wi)
                update = True

for r in res:
    print(*r)
