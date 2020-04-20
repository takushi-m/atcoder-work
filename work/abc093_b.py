a,b,k = map(int, input().split())

s = set()
if a==b:
    s.add(a)
for x in range(a,min(a+k,b)):
    s.add(x)
for x in range(b,max(a,b-k),-1):
    s.add(x)

l = [x for x in s]
l.sort()
for x in l:
    print(x)