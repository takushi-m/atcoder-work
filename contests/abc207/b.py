a,b,c,d = map(int, input().split())

res = 0
sb = a
sr = 0
while sb>sr*d:
    sb += b
    sr += c
    res += 1
    if res>=10**6:
        print(-1)
        exit()
print(res)