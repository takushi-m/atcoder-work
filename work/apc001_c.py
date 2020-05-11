n = int(input())

li = 0
print(li)
ls = input()
if ls=="Vacant":
    exit()

ri = n-1
print(ri)
rs = input()
if rs=="Vacant":
    exit()

while ri>li:
    mid = (ri+li)//2
    print(mid)
    s = input()

    if s=="Vacant":
        exit()
    
    if (mid-li)%2==0:
        if s!=ls:
            ri = mid
            rs = s
        else:
            li = mid
            ls = s
    else:
        if s!=ls:
            li = mid
            ls = s
        else:
            ri = mid
            rs = s
