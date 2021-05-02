n = int(input())
al = list(map(int, input().split()))
al.sort()
q = int(input())
bl = [int(input()) for _ in range(q)]

def score(b):
    ng = -1
    ok = n

    while abs(ng-ok)>1:
        m = (ok+ng)//2

        if al[m]>b:
            ok = m
        else:
            ng = m
    
    idx = ok
    if idx==0:
        return abs(al[idx]-b)
    elif idx==n:
        return abs(al[-1]-b)
    else:
        return min(abs(al[idx]-b), abs(al[idx-1]-b))

for b in bl:
    print(score(b))
