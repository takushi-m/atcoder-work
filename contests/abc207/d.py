from math import sqrt, atan2, cos, sin

n = int(input())
s = [list(map(float, input().split())) for _ in range(n)]
t = [list(map(float, input().split())) for _ in range(n)]

mx,my = 0.0, 0.0
for x,y in s:
    mx += x
    my += y
mx /= n
my /= n
for i in range(n):
    s[i] = [s[i][0]-mx,s[i][1]-my]


mx,my = 0.0, 0.0
for x,y in t:
    mx += x
    my += y
mx /= n
my /= n
for i in range(n):
    t[i] = [t[i][0]-mx,t[i][1]-my]

def check(theta):
    ss = [
        [
            s[i][0]*cos(theta)-s[i][1]*sin(theta), 
            s[i][0]*sin(theta)+s[i][1]*cos(theta)
        ]
        for i
        in range(n)
    ]
    tt = [[t[i][0], t[i][1]] for i in range(n)]

    ft = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not ft[j] and abs(ss[i][0]-tt[j][0])<10**-6 and abs(ss[i][1]-tt[j][1])<10**-6:
                ft[j] = True
                break
    # print(ft)
    return all(ft)


for i in range(n):
    for j in range(n):

        ts = atan2(s[i][1],s[i][0])
        tt = atan2(t[j][1],t[j][0])
        theta = tt - ts
        if check(theta):
            print("Yes")
            exit()
print("No")