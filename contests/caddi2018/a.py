# -*- coding: utf-8 -*-
n,p = map(int, input().split())

# is_prime = list(range(n+1))
# is_prime[1] = 0
# for i in range(2,n+1):
#     if i*i>n+1:
#         break
#     if is_prime[i]:
#         for x in range(2*i,n+1,i):
#             is_prime[x] = 0
# primes = [p for p in is_prime if p!=0]

div = {}
for i in range(2,p+1):
    if p%i==0:
        while p%i==0:
            if i not in div:
                div[i] = 0
            div[i] += 1
            p //= i
    if i*i>p:
        if p>1:
            if p not in div:
                div[p] = 0
            div[p] += 1
        break

res = 1
for r in div.keys():
    while div[r]>=n:
        res *= r
        div[r] -= n

print(res)
