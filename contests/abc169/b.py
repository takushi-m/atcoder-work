n = int(input())
al = list(map(int, input().split()))

if 0 in al:
    print(0)
    exit()

res = 1
for a in al:
    res *= a
    if res>10**18:
        print(-1)
        exit()
print(res)