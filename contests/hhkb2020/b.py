h,w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for hi in range(h):
    for wi in range(w):
        for dh,dw in [[1,0],[0,-1],[-1,0],[0,1]]:
            hh = hi + dh
            ww = wi + dw
            if h>hh>=0 and w>ww>=0:
                if s[hi][wi]=="." and s[hh][ww]==".":
                    ans += 1
print(ans//2)