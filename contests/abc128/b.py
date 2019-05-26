n = int(input())
sp = {}
for i in range(n):
    s,p = input().split()
    p = int(p)
    if s not in sp:
        sp[s] = []
    sp[s].append((p,i+1))

keys = list(sp.keys())
keys.sort()

for k in keys:
    sp[k].sort(reverse=True)
    for p,i in sp[k]:
        print(i)