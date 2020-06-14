n = int(input())
al = list(map(int, input().split()))

cnt = [0]*(10**6+10)
for a in al:
    if cnt[a]>1:
        continue
    for i in range(0,10**6+10,a):
        cnt[i] += 1

res = 0
for a in al:
    if cnt[a]==1:
        res += 1
print(res)