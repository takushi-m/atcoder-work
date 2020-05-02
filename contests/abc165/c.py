n,m,q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

def calc(l):
    res = 0
    for a,b,c,d in abcd:
        if l[b-1]-l[a-1]==c:
            res += d
    # print(l,res)
    return res

def f(l):
    if len(l)==n:
        return calc(l)
    
    res = 0
    for x in range(l[-1],m+1):
        res = max(res, f(l+[x]))
    return res

res = 0
for x in range(1,m+1):
    res = max(res, f([x]))
print(res)