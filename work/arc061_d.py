# -*- coding: utf-8 -*-
h,w,n = map(int, input().split())

cube = {}
for _ in range(n):
    a,b = map(int, input().split())
    for k in range(3):
        for l in range(3):
            if h-2>=a-k>0 and w-2>=b-l>0:
                box = "-".join([str(a-k), str(b-l)])
                if box not in cube:
                    cube[box] = 0
                cube[box] += 1
# print(cube)
ret = [0 for _ in range(10)]
cnt = 0
for v in cube.values():
    ret[v] += 1
    cnt += 1
ret[0] = (h-2)*(w-2) - cnt

for r in ret:
    print(r)
