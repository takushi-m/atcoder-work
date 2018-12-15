# -*- coding: utf-8 -*-
q = int(input())
ql = []
R = 0
for _ in range(q):
    l,r = map(int, input().split())
    ql.append((l,r))
    R = max(R,r)
R += 1

is_prime = list(range(R+1))
is_prime[1] = 0
for n in range(2,R+1):
    if n*n>R+1:
        break
    if is_prime[n]:
        for x in range(2*n,R+1,n):
            is_prime[x] = 0

primes = [p for p in is_prime if p!=0]

like2017 = [0]*(R+1)
for i in range(R):
    if i%2==1 and (i in primes) and ((i+1)//2 in primes):
        like2017[i+1] = like2017[i] + 1
    else:
        like2017[i+1] = like2017[i]

for (l,r) in ql:
    print(like2017[r+1] - like2017[l])
