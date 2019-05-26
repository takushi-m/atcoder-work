n,k = map(int, input().split())
vl = list(map(int, input().split()))

accl = [0]*(n+1)
for i in range(n):
    accl[i+1] = accl[i]+vl[i]

accr = [0]*(n+1)
for i in range(n,0,-1):
    accr[i-1] = accr[i]+vl[i-1]

sl = [0]*(k+1)
for si in range(1,k+1):
    