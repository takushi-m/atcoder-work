N = int(input())

A = []
line = input().split(" ")
A.append(list(map(lambda x:int(x), line)))
line = input().split(" ")
A.append(list(map(lambda x:int(x), line)))

def count(n):
    ret = 0
    for i in range(0,max(n,1)):
        ret += A[0][i]
    for i in range(max(n-1,0),N):
        ret += A[1][i]
    return ret

l = []
for n in range(N):
    l.append(count(n))

print(max(l))
