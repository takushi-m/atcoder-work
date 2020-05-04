n,k = map(int, input().split())
s = set(range(1,n+1))

for _ in range(k):
    d = int(input())
    for a in list(map(int, input().split())):
        if a in s:
            s.remove(a)
print(len(s))