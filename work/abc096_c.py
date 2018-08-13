# -*- coding: utf-8 -*-
line = input().split(" ")
h = int(line[0])
w = int(line[1])

s = []

for _ in range(h):
    s.append(input())

diff = [
    [0,1]
    ,[0,-1]
    ,[1,0]
    ,[-1,0]
]
for hi in range(h):
    for wi in range(w):
        if s[hi][wi]=="#":
            flag = False
            for d in diff:
                if h>hi+d[0]>=0 and w>wi+d[1]>=0:
                    if s[hi+d[0]][wi+d[1]]=="#":
                        flag = True
            if not flag:
                print("No")
                exit()

print("Yes")
