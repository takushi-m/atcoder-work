n,m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]


if n==1:
    for x in range(10):
        x = str(x)
        flag = True
        for s,c in sc:
            s -= 1
            if int(x[s])!=c:
                flag = False
                break
        if flag:
            print(x)
            exit()
elif n==2:
    for x in range(10,100):
        x = str(x)
        flag = True
        for s,c in sc:
            s -= 1
            if int(x[s])!=c:
                flag = False
                break
        if flag:
            print(x)
            exit()
elif n==3:
    for x in range(100,1000):
        x = str(x)
        flag = True
        for s,c in sc:
            s -= 1
            if int(x[s])!=c:
                flag = False
                break
        if flag:
            print(x)
            exit()
print(-1)