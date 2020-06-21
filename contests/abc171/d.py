n = int(input())
d = {}
for a in list(map(int, input().split())):
    if a not in d:
        d[a] = 0
    d[a] += 1
r = sum(k*d[k] for k in d.keys())

q = int(input())
for _ in range(q):
    b,c = map(int, input().split())
    if b not in d:
        pass
    elif c not in d:
        d[c] = d[b]
        r = r - b*d[b] + c*d[c]
    else:
        d[c] += d[b]
        r = r - b*d[b] + c*d[b]
    d[b] = 0
    print(r)