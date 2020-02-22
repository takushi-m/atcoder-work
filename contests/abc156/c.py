n = int(input())
xl = list(map(int, input().split()))
xl.sort()

def cost(p):
    res = 0
    for x in xl:
        res += (x-p)**2
    return res

res = 10**9
for p in range(xl[0],xl[-1]+1):
    res = min(res, cost(p))

print(res)
