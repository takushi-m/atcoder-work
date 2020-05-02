h,w = map(int, input().split())
sl = [list(input()) for _ in range(h)]

dp = [[0]*w for _ in range(h)]

for hi in range(h):
    for wi in range(w):
        if hi==0 and wi==0:
            continue
        dh = 10**9
        if hi-1>=0:
            if sl[hi][wi]=="#" and sl[hi-1][wi]==".":
                dh = dp[hi-1][wi] + 1
            else:
                dh = dp[hi-1][wi]
        dw = 10**9
        if wi-1>=0:
            if sl[hi][wi]=="#" and sl[hi][wi-1]==".":
                dw = dp[hi][wi-1] + 1
            else:
                dw = dp[hi][wi-1]

        dp[hi][wi] = min(dh,dw)

res = dp[h-1][w-1]
if sl[0][0]=="#":
    res += 1
print(res)