from collections import defaultdict

n = int(input())
s = list(input())
q = int(input())
ql = [input().split() for _ in range(q)]

w = 800
sl = []
dl = []
for i in range((n+w-1)//w):
    ss = s[i*w:min((i+1)*w,n)]
    dl.append(set(ss))
    sl.append(ss)
if len(dl)%2==1:
    dl.append(set())
dl2 = []
for i in range(len(dl)//2):
    dl2.append(dl[2*i] | dl[2*i+1])
for i in range(q):
    if ql[i][0]=="1":
        idx = int(ql[i][1])-1
        c = ql[i][2]

        ss = sl[idx//w]
        ss[idx%w] = c
        s[idx] = c
        sl[idx//w] = ss
        dl[idx//w] = set(ss)
        if (idx//w)%2==0:
            dl2[idx//w//2] = dl[idx//w] | dl[idx//w+1]
        else:
            dl2[idx//w//2] = dl[idx//w-1] | dl[idx//w]
    else:
        l = int(ql[i][1])-1
        r = int(ql[i][2])-1

        li = l//w
        ri = r//w
        if abs(li-ri)<2:
            print(len(set(s[l:r+1])))
        else:
            u = set(sl[li][l%w:])
            u |= set(sl[ri][:r%w+1])
            if (li+1)%2==1:
                u |= dl[li+1]
                li += 1
            if (ri-1)%2==0:
                u |= dl[ri-1]
                ri -= 1
            for j in range(li+1,ri,2):
                u |= dl2[j//2]
            print(len(u))
