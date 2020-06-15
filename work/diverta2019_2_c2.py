n = int(input())
al = list(map(int, input().split()))
al.sort()

if n==2:
    print(al[1]-al[0])
    print(al[1],al[0])
    exit()

res = []
neg = []
pos = []
for a in al:
    if a>=0:
        pos.append(a)
    else:
        neg.append(a)

if len(pos)==0:
    res.append((neg[-1],neg[-2]))
    pos.append(neg[-1]-neg[-2])
    neg = neg[:-2]
if len(neg)==0:
    res.append((pos[0],pos[1]))
    neg.append(pos[0]-pos[1])
    pos = pos[2:]


# len(pos)>0 and len(neg)>0
n = neg[0]
for i in range(1,len(pos)):
    res.append((n,pos[i]))
    n = n - pos[i]
p = pos[0]
for i in range(1,len(neg)):
    res.append((p,neg[i]))
    p = p - neg[i]
res.append((p,n))
print(p-n)
for x,y in res:
    print(x,y)