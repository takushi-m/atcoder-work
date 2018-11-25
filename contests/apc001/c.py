# coding=utf-8

def bs(l, u, c):
    if c[0]=="V":
        exit()
    h = l + (u-l)//2
    print(str(h))
    x = input()
    if x[0]=="V":
        exit()
    elif (h-l)%2==0 and x!=c:
        return bs(l, h-1, c)
    elif (h-l)%2==1 and x==c:
        return bs(l, h-1, c)
    else:
        print(str(h+1))
        x = input()
        return bs(h+1, u, x)


N = int(input())

print("0")
x = input()

bs(0,N-1,x)
