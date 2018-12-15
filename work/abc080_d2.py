# -*- coding: utf-8 -*-
from operator import itemgetter

N,C = map(int, input().split())
record = []
for _ in range(N):
    s,t,c = map(int, input().split())
    record.append((s,t,c))
record.sort(key=itemgetter(1,0,2))

def can_record(k):
    slots = [(-1,-1)]*k  # (end_time, channel)

    for r in record:
        idx = -1
        t = -1
        for i in range(k):
            end_time, channel = slots[i]
            if channel==r[2]:
                if end_time<=r[0]:
                    if t<=end_time:
                        t = end_time
                        idx = i
            else:
                if end_time<r[0]:
                    if t<=end_time:
                        t = end_time
                        idx = i
        if idx==-1:
            return False
        else:
            slots[idx] = (r[1],r[2])
    return True

for k in range(1,C+1):
    if can_record(k):
        print(k)
        break
