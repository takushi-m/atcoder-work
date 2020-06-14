x,n = map(int, input().split())
pl = list(map(int, input().split()))

res = -100
for r in range(-100,200):
    if r not in pl:
        if abs(x-r)<abs(x-res):
            res = r
print(res)