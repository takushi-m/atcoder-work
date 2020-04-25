n,m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

def dist(a,b,c,d):
    return abs(a-c)+abs(b-d)

for a,b in ab:
    idx = 0
    for i in range(m):
        if dist(a,b,cd[i][0],cd[i][1]) < dist(a,b,cd[idx][0],cd[idx][1]):
            idx = i
    print(idx+1)