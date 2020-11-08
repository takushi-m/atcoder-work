n = int(input())
al = list(map(int, input().split()))

res = 0
cnt = 0
for k in range(2,1001):
    c = 0
    for a in al:
        if a%k==0:
            c += 1
    if c>cnt:
        cnt = c
        res = k
print(res)