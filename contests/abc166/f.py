n,a,b,c = map(int, input().split())
d = {}
d["A"] = a
d["B"] = b
d["C"] = c

pl = [input() for _ in range(n)]

res = []
for i in range(n):
    p = pl[i]
    if d[p[0]]==d[p[1]]==0:
        print("No")
        exit()
    elif d[p[0]]==0:
        res.append(p[0])
        d[p[0]] += 1
        d[p[1]] -= 1
    elif d[p[1]]==0:
        res.append(p[1])
        d[p[0]] -= 1
        d[p[1]] += 1
    elif i==n-1:
        res.append(p[0])
    elif p[0] in pl[i+1]:
        res.append(p[0])
        d[p[0]] += 1
        d[p[1]] -= 1
    else:
        res.append(p[1])
        d[p[0]] -= 1
        d[p[1]] += 1

    



print("Yes")
for p in res:
    print(p)
