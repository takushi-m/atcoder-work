N,L = map(int, input().split())
K = int(input())
al = list(map(int, input().split()))

def check(l):
    if l<1:
        return True
    if l>L:
        return False
    
    cnt = 0
    prev = 0
    i = 0
    while i<N:
        while i<N and al[i]-prev<l:
            i += 1
        

        if cnt==K or i==N:
            break
        cnt += 1
        prev = al[i]

    return L-prev>=l and cnt == K

ok = 0
ng = L
while abs(ok-ng)>1:
    mid = (ok+ng)//2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)