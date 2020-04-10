n,m = map(int, input().split())

al = [list(input()) for _ in range(n)]
bl = [list(input()) for _ in range(m)]

def same(h,w):
    for hi in range(m):
        for wi in range(m):
            if al[h+hi][w+wi]!=bl[hi][wi]:
                return False
    return True


for hi in range(n-m+1):
    for wi in range(n-m+1):
        if same(hi,wi):
            print("Yes")
            exit()
print("No")