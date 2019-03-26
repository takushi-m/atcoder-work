# -*- coding: utf-8 -*-
h = 10
w = 10
d = []
for _ in range(h):
    line = list(input())
    d.append(line)

def check():
    mark = [[False]*w for _ in range(h)]
    for hi in range(h):
        for wi in range(w):
            if d[hi][wi]=="o":
                sh = hi
                sw = wi

    st = [(sh,sw)]
    while len(st)>0:
        hi,wi = st.pop()
        mark[hi][wi] = True
        for dh,dw in [[0,1],[1,0],[0,-1],[-1,0]]:
            if h>hi+dh>=0 and w>wi+dw>=0:
                if d[hi+dh][wi+dw]=="o" and not mark[hi+dh][wi+dw]:
                    st.append((hi+dh, wi+dw))
    for hi in range(h):
        for wi in range(w):
            if d[hi][wi]=="o" and not mark[hi][wi]:
                return False
    return True


for hi in range(h):
    for wi in range(w):
        if d[hi][wi]=="x":
            d[hi][wi] = "o"
            if check():
                print("YES")
                exit()
            d[hi][wi] = "x"

print("NO")
