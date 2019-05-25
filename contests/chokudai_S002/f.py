n = int(input())
s = set()
for _ in range(n):
    a,b = map(int, input().split())
    s.add((max(a,b), min(a,b)))
print(len(s))