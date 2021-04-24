n = int(input())
s = list(input())
s1 = s[:n]
s2 = s[n:]
q = int(input())

for _ in range(q):
    t,a,b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if a<n and b<n:
            s1[a],s1[b] = s1[b],s1[a]
        elif a>=n and b>=n:
            s2[a-n],s2[b-n] = s2[b-n],s2[a-n]
        else:
            s1[a],s2[b-n] = s2[b-n],s1[a]
    else:
        s1,s2 = s2,s1

print("".join(s1+s2))