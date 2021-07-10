from collections import deque

n = int(input())
sl = [input() for _ in range(n)]

f = {}
for s in sl:
    x = s[-3:]
    f[x] = []
for s in sl:
    x = s[:3]
    if x in f:
        f[x].append(s)

b = {}
for s in sl:
    x = s[:3]
    b[x] = []
for s in sl:
    x = s[-3:]
    if x in b:
        b[x].append(s)

q = deque([])
ans = {}
for s in sl:
    x = s[-3:]
    if len(f[x])==0: # 次がない
        ans[s] = "Takahashi"
        xb = s[:3]
        if xb in b:
            for t in b[xb]:
                q.append(t)

while len(q)>0:
    s = q.popleft()

    x = s[-3:]
    if all(y in ans for y in f[x]):
        for y in f[x]:
            if ans[y] == "Aoki":
                ans[s] = "Takahashi"
                xb = s[:3]
                if xb in b:
                    for t in b[xb]:
                        q.append(t)
                break
        if s not in ans:
            ans[s] = "Aoki"
            xb = s[:3]
            if xb in b:
                for t in b[xb]:
                    q.append(t)

for s in sl:
    if s in ans:
        print(ans[s])
    else:
        print("Draw")