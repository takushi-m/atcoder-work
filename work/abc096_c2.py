# -*- coding: utf-8 -*-
h,w = map(int, input().split())
s = [["." for _ in range(w+2)]]
for _ in range(h):
    line = list(input())
    s.append(["."]+line+["."])
s.append(["." for _ in range(w+2)])
diff = [
    [1,0]
    ,[0,1]
    ,[-1,0]
    ,[0,-1]
]
def dfs(hi,wi):
    stack = [(hi,wi)]
    while len(stack)>0:
        hi,wi = stack.pop()
        s[hi][wi] = "."
        for d in diff:
            if s[hi+d[0]][wi+d[1]] == "#":
                stack.append((hi+d[0], wi+d[1]))

for hi in range(1,h+1):
    for wi in range(1,w+1):
        if s[hi][wi] == "#":
            f = False
            for d in diff:
                f = f or s[hi+d[0]][wi+d[1]]=="#"
            if f:
                dfs(hi, wi)

for hi in range(1,h+1):
    for wi in range(1,w+2):
        if s[hi][wi] == "#":
            print("No")
            exit()
print("Yes")
