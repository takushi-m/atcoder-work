n = int(input())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(n)]


s = []
sc = []
t = []
tc = []
for i in range(n):
    for j in range(n):
        if sl[i][j]=="#":
            s.append((i,j))
        else:
            sc.append((i,j))

        if tl[i][j]=="#":
            t.append((i,j))
        else:
            tc.append((i,j))

if len(s)!=len(t):
    print("No")
    exit()

if len(s)>n*n//2:
    s = sc
    t = tc

n = len(s)
if n==0:
    print("Yes")
    exit()

from math import pi, atan2, cos, sin

msx,msy = 0.0, 0.0
mtx,mty = 0.0, 0.0
for i in range(n):
    x,y = s[i][0],s[i][1]
    msx += x
    msy += y

    x,y = t[i][0],t[i][1]
    mtx += x
    mty += y
msx /= n
msy /= n
mtx /= n
mty /= n
for i in range(n):
    s[i] = [s[i][0]-msx,s[i][1]-msy]
    t[i] = [t[i][0]-mtx,t[i][1]-mty]

def check(theta):
    ss = [
        [
            s[i][0]*cos(theta)-s[i][1]*sin(theta), 
            s[i][0]*sin(theta)+s[i][1]*cos(theta)
        ]
        for i
        in range(n)
    ]
    tt = t

    ft = [False for _ in range(n)]
    for i in range(n):
        f = False
        for j in range(n):
            if not ft[j] and abs(ss[i][0]-tt[j][0])<10**-6 and abs(ss[i][1]-tt[j][1])<10**-6:
                ft[j] = True
                f = True
                break
        if not f:
            return False
    # print(ft)
    return True

for theta in [0, pi/2, pi, 3*pi/2]:
    if check(theta):
        print("Yes")
        exit()
print("No")