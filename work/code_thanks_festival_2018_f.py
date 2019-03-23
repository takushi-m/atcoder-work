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
def check(ul):
    used = [False for _ in range(n)]
    cnt = 0
    for u in ul:
        used[u-1] = True
    if used[root]:
        if ul[-1]-1 != root:
            return False
    for i in range(m-1,-1,-1):
        v = ul[i]-1
        st = [(root,1)]
        while len(st)>0:
            u,c = st.pop()
            if u==v:
                used[u] = False
                cnt += c
                break
            if u not in edge:
                continue
            for w in edge[u]:
                if w==v or not used[w]:
                    st.append((w,c+1))
        if used[v]:
            return False
    return cnt<=k

print(check([1,3]))
