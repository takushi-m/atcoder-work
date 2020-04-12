n = int(input())
al = list(map(int, input().split()))

acc = [0]*(n+2)
for i in range(n):
    acc[i+2] += acc[i]+al[i]

def f(acc,s):
    res = -1
    for i in range(s,n,2):
        res = max(res, acc[i]-acc[s] + acc[-1]-acc[i+1])
    return res

if n%2==0:
    print(f(acc,0))
    exit()

res = -1
x = 0
for i in range(0,n,2):
    res = max(res, x+f(acc,i+1))
    x += al[i]

print(res)
