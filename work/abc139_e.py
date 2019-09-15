# -*- coding: utf-8 -*-
def make(x,y):
    if x<y:
        return str(x)+"_"+str(y)
    else:
        return str(y)+"_"+str(x)


n = int(input())
s = set()
edge = {}
redge = {}
for x in range(n):
    al = list(map(lambda x:int(x)-1, input().split()))
    s.add(make(x,al[0]))
    for i in range(len(al)-1):
        v = make(x,al[i])
        u = make(x,al[i+1])

        if v not in edge:
            edge[v] = []
        edge[v].append(u)

        if u not in redge:
            redge[u] = 0
        redge[u] += 1

s2 = set()
for k in s:
    if k not in redge:
        s2.add(k)
s = s2

res = 0
while len(s)>0:
    res += 1
    s2 = set()
    for v in s:
        if v not in edge:
            continue
        for u in edge[v]:
            redge[u] -= 1
            if redge[u]==0:
                s2.add(u)
                del redge[u]
    s = s2

for v in redge:
    print(-1)
    exit()
print(res)
