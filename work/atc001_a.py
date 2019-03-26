# -*- coding: utf-8 -*-
h,w = map(int, input().split())
d = []

for hi in range(h):
    line = list(input())
    d.append(line)
    for wi in range(w):
        c = line[wi]
        if c=="s":
            sh = hi
            sw = wi

used = [[False]*w for _ in range(h)]
st = [(sh,sw)]
while len(st)>0:
    hi,wi = st.pop()
    used[hi][wi] = True
    c = d[hi][wi]
    if c=="g":
        print("Yes")
        exit()
    for dh,dw in [[0,1],[1,0],[0,-1],[-1,0]]:
        if h>hi+dh>=0 and w>wi+dw>=0:
            if not used[hi+dh][wi+dw] and d[hi+dh][wi+dw]!="#":
                st.append((hi+dh, wi+dw))

print("No")
