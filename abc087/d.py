# coding=utf-8

line = input().split(" ")
N = int(line[0])
M = int(line[1])

if M==0:
    print("Yes")
    exit()

l = []
for _ in range(M):
    line = input().split(" ")
    l.append((
        int(line[0])-1
        ,int(line[1])-1
        ,int(line[2])
    ))
l.sort()
o = l[0][0]
for i in range(M):
    l[i] = (
        l[i][0]-o
        ,l[i][1]-o
        ,l[i][2]
    )

def check(l):
    nl = [None for x in range(N)]
    nl[0] = 0

    flag = True
    while flag:
        flag = False
        ll = []
        for c in l:
            if nl[c[0]]!=None and nl[c[0]]>=0 and nl[c[1]]==None:
                nl[c[1]] = nl[c[0]]+c[2]
            elif nl[c[0]]==None and nl[c[1]]!=None and nl[c[1]]>=0:
                nl[c[0]] = nl[c[1]]-c[2]
            elif nl[c[0]]!=None and nl[c[0]]>=0 and nl[c[1]]!=None and nl[c[1]]>=0:
                if nl[c[1]]-nl[c[0]]==c[2]:
                    pass
                else:
                    print("No")
                    exit()
            else:
                ll.append(c)
                flag = True
        if len(l)==len(ll):
            break
        else:
            l = ll.copy()
    for x in nl:
        if x!=None and x<0:
            print("No")
            exit()
    return l

while len(l)>0:
    l = check(l)
    if len(l)==0:
        break
    l.sort()
    o = l[0][0]
    for i in range(len(l)):
        l[i] = (
            l[i][0]-o
            ,l[i][1]-o
            ,l[i][2]
        )


print("Yes")
