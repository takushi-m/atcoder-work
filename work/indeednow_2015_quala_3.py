def upper_bound(al,key):
    def isOk(a):
        return a>key

    ng = -1
    ok = len(al)
    while ok-ng>1:
        mid = (ok+ng)//2
        if isOk(al[mid]):
            ok = mid
        else:
            ng = mid
    return ok

n = int(input())
sl = []
for _ in range(n):
    s = int(input())
    if s>0:
        sl.append(s)
q = int(input())
ql = [int(input()) for _ in range(q)]

sl.sort()
for k in ql:
    if len(sl)==0:
        print(0)
    elif k==0:
        print(sl[-1]+1)
    elif k>=len(sl):
        print(0)
    elif sl[-k]>sl[-k-1]:
        print(sl[-k-1]+1)
    else:
        idx = upper_bound(sl, sl[-k])
        if idx==len(sl):
            print(sl[-1]+1)
        else:
            print(sl[idx-1]+1)