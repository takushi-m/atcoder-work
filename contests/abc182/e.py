from pprint import pprint

h,w,n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

lamp = [[0]*w for _ in range(h)]
block = [[0]*w for _ in range(h)]
for a,b in ab:
    lamp[a-1][b-1] = 1
for c,d in cd:
    block[c-1][d-1] = 1

n = [[0]*w for _ in range(h)]
for hi in range(h):
    for wi in range(w):
        n[hi][wi] += lamp[hi][wi]

for hi in range(h):
    c = 0
    for wi in range(w-1):
        c += lamp[hi][wi]
        if block[hi][wi]>0:
            c = 0
        if block[hi][wi+1]==0:
            n[hi][wi+1] += c

    c = 0
    for wi in range(w-1,0,-1):
        c += lamp[hi][wi]
        if block[hi][wi]>0:
            c = 0
        if block[hi][wi-1]==0:
            n[hi][wi-1] += c

for wi in range(w):
    c = 0
    for hi in range(h-1):
        c += lamp[hi][wi]
        if block[hi][wi]>0:
            c = 0
        if block[hi+1][wi]==0:
            n[hi+1][wi] += c
    
    c = 0
    for hi in range(h-1,0,-1):
        c += lamp[hi][wi]
        if block[hi][wi]>0:
            c = 0
        if block[hi-1][wi]==0:
            n[hi-1][wi] += c

# pprint(lamp)
# pprint(block)
# pprint(n)

res = 0
for hi in range(h):
    for wi in range(w):
        if block[hi][wi]==0:
            if n[hi][wi]>0:
                res += 1
print(res)