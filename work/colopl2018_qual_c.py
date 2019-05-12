# -*- coding: utf-8 -*-

def check(l):
    if len(l)<2:
        return True
    for p in [2,3,5,7,11,13,17,19,23,29,31]:
        cnt = 0
        for x in l:
            if x%p==0:
                cnt += 1
            if cnt>1:
                return False
    return True

a,b = map(int, input().split())
nl = []
nl2 = []
nl3 = []

for i in range(a,b+1):
    if i%2==0:
        nl2.append(i)
    elif i%3==0:
        nl3.append(i)
    else:
        nl.append(i)

cnt = 0
for i in range(len(nl2)+1):
    if i==len(nl2):
        n2 = []
    else:
        n2 = [nl2[i]]

    for j in range(len(nl3)+1):
        if j==len(nl3):
            n3 = []
        else:
            n3 = [nl3[j]]

        for k in range(2**len(nl)):
            n = []
            for idx in range(len(nl)):
                if ((k>>idx)&1)==1:
                    n.append(nl[idx])
            if check(n+n2+n3):
                cnt += 1

print(cnt)
