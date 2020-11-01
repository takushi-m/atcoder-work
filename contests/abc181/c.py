n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if i==k or j==k:
                continue
                
            x1,y1 = xy[i]
            x2,y2 = xy[j]
            x3,y3 = xy[k]

            if x1==x2:
                if x1==x3:
                    print("Yes")
                    exit()
                continue
            if y1==y2:
                if y1==y3:
                    print("Yes")
                    exit()
                continue

            a = (y2-y1)/(x2-x1)
            #y1 = a*x1 + b
            b = y1 - a*x1

            if y3 == a*x3+b:
                print("Yes")
                exit()
print("No")