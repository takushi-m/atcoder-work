n = int(input())
al = [int(input()) for _ in range(n)]

d = {}
s = -1
idx = -1
for a in sorted(al):
    if a!=s:
        s = a
        idx += 1
    d[s] = idx

for a in al:
    print(d[a])