n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

d = {}
for i in range(n):
    x,y = xy[i]
    if x not in d:
        d[x] = set()
    d[x].add(y)
# print(d)
res = 0
xs = d.keys()
for x1 in xs:
    for x2 in xs:
        if x1==x2:
            continue
        
        for y1 in d[x1]:
            for y2 in d[x1]:
                if y1==y2:
                    continue

                if y1 in d[x2] and y2 in d[x2]:
                    res += 1
print(res//4)