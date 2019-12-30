# -*- coding: utf-8 -*-
s = input()
n = len(s)

cnt = 0
for i in range(1,n-4):
    s1 = s[:i]
    for j in range(i+1,n-3):
        s2= s[i:j]
        if s2!=s[-(j-i):]:
            continue
        for k in range(j+1,n-2):
            s3 = s[j:k]
            if k+len(s3)+len(s2)<n and s3==s[k:k+len(s3)]:
                cnt += 1

print(cnt)