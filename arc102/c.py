# -*- coding: utf-8 -*-
n,k = [int(x) for x in input().split()]

ret = 0
for b in range(1,n+1):
    r = k - b%k
    # print(b,r)
    if r==k:
        # print("|",(n//k)**2)
        ret += (n//k)**2
    elif (2*r)%k==0:
        if r<=n%k:
            # print("*", (n//k+1)**2)
            ret += (n//k+1)**2
        else:
            # print("*", (n//k)**2)
            ret += (n//k)**2
print(ret)
# print("---")
# ret = 0
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         for c in range(1,n+1):
#             if (a+b)%k==0 and (b+c)%k==0 and (a+c)%k==0:
#                 # print(a,b,c)
#                 ret += 1
# print(ret)
