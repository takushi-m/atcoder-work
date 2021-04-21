def check(n,x):
    p = 0
    for s in range(n-1,-1,-1):
        if x>>s & 1 == 0:
            p += 1
        else:
            p -= 1
        
        if p<0:
            return False
    return p==0

def p(n,x):
    s = []
    for i in range(n-1,-1,-1):
        if x>>i & 1 == 0:
            s.append("(")
        else:
            s.append(")")
    return "".join(s)

n = int(input())
if n%2==1:
    exit()

ret = []
for x in range(1<<n):
    if check(n,x):
        ret.append(p(n,x))

ret.sort()
for s in ret:
    print(s)