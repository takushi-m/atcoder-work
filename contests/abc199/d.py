n,m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

gg = []
checked = [False]*n
while not all(checked):
    s = 0
    for i in range(n):
        if not checked[i]:
            s = i
            break

    elm = [s]
    checked[s] = True
    q = [s]
    while len(q)>0:
        v = q.pop()
        for u in g[v]:
            if not checked[u]:
                checked[u] = True
                elm.append(u)
                q.append(u)
    gg.append(elm)


def count(start, elm):
    counted = set([])

    def check(colors, v, c):
        for u in g[v]:
            if colors[u]==c:
                return False
        return True

    def f(colors, v):
        flag = True
        for vv in elm:
            if colors[vv]=="":
                flag = False
                break
        if flag:
            s = "-".join(colors)
            if s in counted:
                return 0
            else:
                counted.add(s)
                return 1
        
        res = 0
        for u in g[v]:
            if colors[u] != "":
                continue

            cc = set(["r","g","b"]) - set([colors[v]])
            for c in cc:
                if check(colors, u, c):
                    colors[u] = c
                    res += f(colors, u)
            colors[u] = ""
        return res

    res = 0
    colors = [""]*n
    for c in ["r","g","b"]:
        colors[start] = c
        res += f(colors, start)
    return res

cnt = []
for elm in gg:
    cnt.append(count(elm[0],elm))

res = 1
for c in cnt:
    res *= c
print(res)