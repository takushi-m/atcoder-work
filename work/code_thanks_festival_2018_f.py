# -*- coding: utf-8 -*-
n,m,k = map(int, input().split())
pl = list(map(int, input().split()))
edge = {}
for i in range(n):
    p = pl[i]-1
    if p==-1:
        root = i
        continue
    if p not in edge:
        edge[p] = []
    edge[p].append(i)
print(root)
print(edge)

tree = {}
tree[root] = ([],1)
st = [root]
while len(st)>0:
    v = st.pop()
    cnt = tree[v][1]
    if v not in edge:
        continue
    for u in edge[v]:
        tree[v][0].append(u)
        if u not in tree:
            tree[u] = ([],cnt+1)
        st.append(u)

print(tree)

from itertools import permutations

for l in permutations(range(n), r=m):
    res = 0
    for p in l:
        res += tree[p][1]
    print(l,res)
    if res==k:
        print(*[i+1 for i in l])
        exit()
print(-1)
