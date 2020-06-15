from collections import deque
h,w = map(int, input().split())
al = [input() for _ in range(h)]

inf = 10**9
f = [[inf]*w for _ in range(h)]
q = deque()
for hi in range(h):
    for wi in range(w):
        if al[hi][wi]=="#":
            f[hi][wi] = 0
            q.append((hi,wi))

while len(q)>0:
    hi,wi = q.popleft()
    c = f[hi][wi]

    for dh,dw in [[0,1],[1,0],[0,-1],[-1,0]]:
        nh = hi+dh
        nw = wi+dw
        if h>nh>=0 and w>nw>=0:
            if f[nh][nw]>c+1:
                f[nh][nw] = c+1
                q.append((nh,nw))

res = 0
for hi in range(h):
    for wi in range(w):
        res = max(res,f[hi][wi])
print(res)