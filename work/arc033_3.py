class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0]*(n+1)

    def add(self, idx, w):
        i = idx
        while i<self.n:
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

q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]

bit = BIT(200000+10)
for t,x in tx:
    if t==1:
        bit.add(x,1)
    else:
        l = bit.lower_bound(x)
        print(l)
        bit.add(l,-1)