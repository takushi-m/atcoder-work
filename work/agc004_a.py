a,b,c = map(int, input().split())

res = a*b*c
res = min(res, abs(a*b*(c//2) - a*b*(c-c//2)))
res = min(res, abs(a*(b//2)*c - a*(b-b//2)*c))
res = min(res, abs((a//2)*b*c - (a-a//2)*b*c))
print(res)