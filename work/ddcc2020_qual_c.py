h,w,k = map(int, input().split())
sl = [input() for _ in range(h)]

res = [[0]*w for _ in range(h)]
idx = 1
hi = 0
while hi<h:
    hi2 = hi
    while hi2<h and sl[hi2].count("#")==0:
        hi2 += 1
    c = sl[hi2].count("#")
    hidx = hi2
    if hi2<h:
        hi2 += 1
        while hi2<h and sl[hi2].count("#")==0:
            hi2 += 1

    if c==1:
        for i in range(hi,hi2):
            for j in range(w):
                res[i][j] = idx
        hi = hi2
        idx += 1
    else:
        wi = 0
        while wi<w:
            wi2 = wi
            while wi2<w and sl[hidx][wi2]==".":
                wi2 += 1
            if wi2<w:
                wi2 += 1
                while wi2<w and sl[hidx][wi2]==".":
                    wi2 += 1
            for i in range(hi,hi2):
                for j in range(wi,wi2):
                    res[i][j] = idx
            wi = wi2
            idx += 1
        hi = hi2

for r in res:
    print(" ".join(str(x) for x in r))