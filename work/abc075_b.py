h,w = map(int, input().split())
sl = [list(input()) for _ in range(h)]

for hi in range(h):
    for wi in range(w):
        if sl[hi][wi]=="#":
            continue
        c = 0
        for dh in range(-1,2):
            for dw in range(-1,2):
                if h>hi+dh>=0 and w>wi+dw>=0:
                    if sl[hi+dh][wi+dw]=="#":
                        c += 1
        sl[hi][wi] = str(c)

for l in sl:
    print("".join(l))