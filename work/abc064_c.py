# -*- coding: utf-8 -*-

n = int(input())
a = [int(x) for x in input().split(" ")]

rate = [0 for _ in range(8)]
xx = 0

for x in a:
    if x<400:
        rate[0] += 1
    elif 400<=x and x<800:
        rate[1] += 1
    elif 800<=x and x<1200:
        rate[2] += 1
    elif 1200<=x and x<1600:
        rate[3] += 1
    elif 1600<=x and x<2000:
        rate[4] += 1
    elif 2000<=x and x<2400:
        rate[5] += 1
    elif 2400<=x and x<2800:
        rate[6] += 1
    elif 2800<=x and x<3200:
        rate[7] += 1
    else:
        xx += 1

cnt = 0
for r in rate:
    if r>0:
        cnt += 1
if xx==0:
    print(str(cnt)+" "+str(cnt))
else:
    if cnt<2:
        print("1 "+str(xx+cnt))
    else:
        print(str(cnt)+" "+str(xx+cnt))
