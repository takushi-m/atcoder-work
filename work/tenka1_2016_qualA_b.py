# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(2000)
n,m = map(int, input().split())

tree = {}
for i in range(1,n):
    p = int(input())
    if p not in tree:
        tree[p] = []
    tree[p].append(i)

cnt = [0]*n
for _ in range(m):
    b,c = map(int, input().split())
    cnt[b] = c


def bfs(i):
    if i not in tree:
        return cnt[i]
    l = [bfs(u) for u in tree[i]]
    mn = min(l)
    for u in tree[i]:
        cnt[u] -= mn
    cnt[i] = mn
    return cnt[i]

bfs(0)
cnt[0] *= len(tree[0])
print(sum(cnt))
