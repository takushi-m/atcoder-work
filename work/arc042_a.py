n,m = map(int, input().split())

l = list(range(n-1,-1,-1))
for _ in range(m):
    a = int(input()) - 1
    l.append(a)

l.reverse()

s = set()
for x in l:
    if x not in s:
        print(x+1)
        s.add(x)
