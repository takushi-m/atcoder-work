# coding=utf-8

def lcs(s1,s2):
    table = []
    for _ in range(310):
        table.append([0 for _ in range(310)])

    for y in range(1,len(s1)+1):
        for x in range(1,len(s2)+1):
            match = 0
            if s1[y-1]==s2[x-1]:
                match = 1

            v1 = table[y-1][x-1]+match
            v2 = table[y-1][x]
            v3 = table[y][x-1]
            table[y][x] = max(v1,v2,v3)
    return table[len(s1)][len(s2)]

def log(s,s2):
    # return
    print("---")
    print("s :"+"".join(s))
    print("s2:"+"".join(s2))

s = list(input())
k = int(input())
s2 = s[::-1]

if k>=len(s)//2:
    print(len(s))
    exit(0)

log(s,s2)

ab = set(s)

for i in range(k):
    idx = -1
    char = ""
    r = -1
    rr = lcs(s,s2)
    for j in range(len(s)):
        for x in ab:
            t = s[:]
            t[j] = x
            t2 = t[::-1]
            r2 = lcs(t,t2)
            if r2>r:
                r = r2
                idx = j
                char = x

            if r>rr+1:
                break

    s[idx] = char
    s2 = s[::-1]
    log(s,s2)


print(lcs(s,s2))
