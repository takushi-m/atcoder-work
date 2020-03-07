class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0]*(n+1)

    def add(self, idx, w):
        i = idx
        while i<=self.n:
            self.l[i] += w
            i += i&-i

    def sum(self, idx):
        res = 0
        i = idx
        while i>0:
            res += self.l[i]
            i -= i&-i
        return res

    def lower_bound(self, w):
        if w<=0:
            return 0
        idx = 0
        k = 1
        while k*2<=self.n:
            k *= 2
        while k>0:
            if idx+k<=self.n and self.l[idx+k]<w:
                w -= self.l[idx+k]
                idx += k
            k //= 2
        return idx+1

    def pos(self, idx):
        return self.sum(idx) - self.sum(idx-1)

    def array(self):
        res = []
        for i in range(1,self.n+1):
            res.append(self.pos(i))
        return res

n,m,h = map(int, input().split())
al = list(map(int, input().split()))
q = [input().split() for _ in range(m)]

nmax = n+m
bit = BIT(nmax)
for i in range(n):
    bit.add(i+1, al[i])
n += 1

for i in range(m):
    if q[i][0]=="add":
        a = int(q[i][1])
        bit.add(n,a)
        n += 1
        continue

    x = int(q[i][1])
    l = bit.lower_bound(x-h+1)
    r = bit.lower_bound(x+h)
    # print(bit.array(),x,l,r)
    if l>bit.n:
        print("miss")
    elif bit.sum(l)==bit.sum(min(r,bit.n)):
        print("go")
        a = bit.pos(l)
        bit.add(l,-a)
    else:
        print("stop")
