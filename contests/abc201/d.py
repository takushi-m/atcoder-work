h,w = map(int, input().split())
al = [list(input()) for _ in range(h)]

def f(i,j):
    return 1 if al[i][j]=="+" else -1

dp = [[10**9]*w for _ in range(h)]
for hi in range(h):
    for wi in range(w):
        if (hi+wi)%2==0:
            dp[hi][wi] *= -1

dp[-1][-1] = 0

for hi in range(h-1,-1,-1):
    for wi in range(w-1,-1,-1):
        if hi+1<h:
            if (hi+wi)%2==0:
                dp[hi][wi] = max(dp[hi][wi], dp[hi+1][wi]+f(hi+1,wi))
            else:
                dp[hi][wi] = min(dp[hi][wi], dp[hi+1][wi]-f(hi+1,wi))
        if wi+1<w:
            if (hi+wi)%2==0:
                dp[hi][wi] = max(dp[hi][wi], dp[hi][wi+1]+f(hi,wi+1))
            else:
                dp[hi][wi] = min(dp[hi][wi], dp[hi][wi+1]-f(hi,wi+1))

if dp[0][0]==0:
    print("Draw")
elif dp[0][0]>0:
    print("Takahashi")
else:
    print("Aoki")