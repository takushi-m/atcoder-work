n = int(input())
al = list(map(int, input().split()))

if n==2:
    print(max(al)-min(al))
    print(max(al),min(al))
    exit()

pos = []
neg = []
for a in al:
    if a>=0:
        pos.append(a)
    else:
        neg.append(a)

pos.sort()
neg.sort(reverse=True)
res = []

if len(pos)==0:
    x = neg[0]
    for a in neg[1:]:
        res.append((x,a))
        x -= a
elif len(neg)==0:
    x = pos[0]
    for a in pos[1:-1]:
        res.append((x,a))
        x -= a
    res.append((pos[-1],x))
    x = pos[-1]-x
else:
    p = pos[0]
    pos = pos[1:]

    x = neg[0]
    neg = neg[1:]

    for a in pos:
        res.append((x,a))
        x -= a
    res.append((p,x))
    x = p - x
    for a in neg:
        res.append((x,a))
        x -= a


print(x)
for a,b in res:
    print(a,b)