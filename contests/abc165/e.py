def f(n,m):
    res = []
    s = set(range(1,n+1))
    d = 0
    while True:
        d += 1
    # for d in range(1,m+1):
        x,y = -1,-1
        for a in s:
            b = (a+d)%(n+1)
            if b in s:
                x = a
                y = b
                break
        if x>0 and y>0:
            res.append((x,y))
            s.remove(x)
            s.remove(y)
        if len(res)==m:
            break
    return res

def check(n,ab):
    l = []
    for a,b in ab:
        l.append(a)
        l.append(b)
    if len(l)!=len(set(l)):
        print(1,ab)
        return False
    if len(ab)!=m:
        print(2,ab)
        return False
    p = [x for x in range(1,n+1)]
    d = set()
    for _ in range(n):
        for a,b in ab:
            c = (min(p[a-1],p[b-1]), max(p[a-1],p[b-1]))
            if c in d:
                print(3,c,ab)
                return False
            d.add(c)
        p = [x-1 if x-1>0 else n for x in p]
    return True

if __name__ == "__main__":
    # n,m = map(int, input().split())
    # print(f(n,m))
    n = 100
    for m in range(1,(n-1)//2+1):
        if not check(n, f(n,m)):
            print(n,m)