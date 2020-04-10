k,t = map(int, input().split())
al = list(map(int, input().split()))

al.sort(reverse=True)

x,y = 0,0
for a in al:
    if x<y:
        x += a
    else:
        y += a

res = (max(x,y)-min(x,y)) - 1
print(max(res,0))