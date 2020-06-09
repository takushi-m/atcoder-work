n = int(input())
al = list(map(int, input().split()))

res = [0]*n
for a in al:
    res[a-1] += 1

for r in res:
    print(r)