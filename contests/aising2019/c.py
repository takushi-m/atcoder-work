# -*- coding: utf-8 -*-
h,w = map(int, input().split())
sf = [input() for _ in range(h)]

def candidate(hi,wi):
    for d in [[1,0],[0,1],[-1,0],[0,-1]]:
        dh = hi+d[0]
        dw = wi+d[1]
        if h>dh>=0 and w>dw>=0 and sf[hi][wi]!=sf[dh][dw]:
            return True
    return False

csf = [[False for _ in range(w)] for _ in range(h)]
for hi in range(h):
    for wi in range(w):
        csf[hi][wi] = candidate(hi,wi)
res = 0
used = [[False for _ in range(w)] for _ in range(h)]
for hi in range(h):
    for wi in range(w):
        if used[hi][wi]:
            continue
        st = [(hi,wi,sf[hi][wi])]
        nb = 0
        nw = 0
        # print("===")
        while len(st)>0:
            s = st.pop()
            # print(s)
            if csf[s[0]][s[1]] and not used[s[0]][s[1]]:
                used[s[0]][s[1]] = True
                if s[2] == "#":
                    nb += 1
                else:
                    nw += 1
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    dh = s[0]+d[0]
                    dw = s[1]+d[1]
                    if h>dh>=0 and w>dw>=0 and csf[dh][dw] and not used[dh][dw] and sf[s[0]][s[1]]!=sf[dh][dw]:
                        st.append((dh,dw,sf[dh][dw]))
        res += nb*nw
print(res)
