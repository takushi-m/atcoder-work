# -*- coding: utf-8 -*-
n = int(input())
MAX = 55555
is_prime = [1 for _ in range(MAX+1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, MAX+1):
    if is_prime[i]==0:
        continue
    else:
        for j in range(2*i,MAX+1,i):
            is_prime[j] = 0
primes = [i for i in range(MAX+1) if is_prime[i]==1]

res = []
for i in primes:
    if len(res)==n:
        break
    if i%5==1:
        res.append(i)

print(*res)
