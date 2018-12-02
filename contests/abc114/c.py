# -*- coding: utf-8 -*-
n = int(input())

if n<357:
    print(0)
    exit()

def inc(ary):
    ary[0] += 1
    for i in range(len(ary)-1):
        if ary[i]==0:
            ary[i] = 3
            break
        elif ary[i]==4:
            ary[i] = 5
            break
        elif ary[i]==6:
            ary[i] = 7
            break
        elif ary[i]==8:
            ary[i] = 3
            if ary[i+1]==0:
                ary[i+1] = 3
                break
            else:
                ary[i+1] += 1

cnt = 0
digit = [0 for _ in range(10)]
digit[0] = 3
while True:
    x = int("".join(map(str,reversed(digit))))
    if x>n:
        break
    if 3 in digit and 5 in digit and 7 in digit:
        cnt += 1

    inc(digit)
print(cnt)
