# -*- coding: utf-8 -*-
Q = int(input())
query = []
rmax = -1
for _ in range(Q):
    line = list(map(int, input().split()))
    query.append(line)
    rmax = max(rmax, line[1])

prime = [2]

for x in range(3, rmax+1):
    pflag = True
    for n in prime:
        if x%n==0:
            pflag = False
            break
        if x<n*n:
            break
    if pflag:
        prime.append(x)
# print(prime)
acc = [0 for _ in range(rmax+1)]
for n in range(rmax+1):
    if n in prime and (n+1)//2 in prime:
        acc[n] += 1
    if n<rmax:
        acc[n+1] += acc[n]
# print(acc)
for q in query:
    print(acc[q[1]] - acc[q[0]-1])
