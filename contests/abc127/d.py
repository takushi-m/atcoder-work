from operator import itemgetter

n,m = map(int, input().split())
al = list(map(int, input().split()))
bc = []
for _ in range(m):
    b,c = map(int, input().split())
    bc.append([b,c])


bc.sort(key=itemgetter(1), reverse=True)
al.sort()

i = 0
while len(bc)>0 and i<n:
    b,c = bc.pop(0)

    for j in range(b):
        if i+j<n and al[i+j]<c:
            al[i+j] = c
    i += b

print(sum(al))