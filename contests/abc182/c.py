from itertools import combinations

nl = [int(c) for c in input()]

s = sum(nl)
if s%3==0:
    print(0)
    exit()

k = 100
for r in range(len(nl)-1,0,-1):
    for c in combinations(range(len(nl)), r=r):
        s = 0
        for i in c:
            s += nl[i]
        if s%3==0:
            print(len(nl)-r)
            exit()
print(-1)
