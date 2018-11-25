K = int(input())
A = list(map(lambda x:int(x), input().split(" ")))
A.reverse()

n = [2,2]

for a in A:

    n1 = (n[0]//a+(1 if n[0]%a>0 else 0))*a
    n2 = (n[1]//a)*a
    # print([n,n1,n2,a])
    if n1>n2:
        print("-1")
        exit()
    n[0] = n1
    n[1] = n2+a-1

if len(n)>0:
    print(min(n),max(n))
else:
    print("-1")
