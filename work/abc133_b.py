n,d = map(int, input().split())

xl = [list(map(int, input().split())) for _ in range(n)]

def check(x,y):
    ss = sum([(x[i]-y[i])**2 for i in range(d)])
    i = 0
    while i*i<ss:
        i += 1
    return i*i==ss


res = 0
for i in range(n-1):
    for j in range(i+1,n):
        if check(xl[i],xl[j]):
            res += 1
print(res)
