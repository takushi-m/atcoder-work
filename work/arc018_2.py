from itertools import combinations
# 3点を与えて三角形の面積を計算する
# v = (x,y)
def triS(v1,v2,v3):
    v2 = v2[0]-v1[0],v2[1]-v1[1]
    v3 = v3[0]-v1[0],v3[1]-v1[1]
    
    return abs(v2[0]*v3[1]-v2[1]*v3[0])

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

res = 0
for c in combinations(range(n),3):
    v1,v2,v3 = xy[c[0]],xy[c[1]],xy[c[2]]
    s = triS(v1,v2,v3)
    if s>0 and s%2==0:
        res += 1

print(res)