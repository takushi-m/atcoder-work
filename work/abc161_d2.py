k = int(input())

res = []
q = list(range(1,10))
while len(q)>0:
    a = q.pop()
    res.append(a)
    if a<4*10**10:
        d = a%10
        if d>0:
            q.append(10*a+d-1)
        q.append(10*a+d)
        if d<9:
            q.append(10*a+d+1)

res.sort()
print(res[k-1])