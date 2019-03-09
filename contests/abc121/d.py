# -*- coding: utf-8 -*-

def f(a,b):
    res = 0
    for i in range(50):
        sa = (1<<i) * (a//(2*(1<<i)))
        t = (a)%(2*(1<<i))
        if t>0:
            if t > (1<<i):
                sa += t - (1<<i)

        sb = (1<<i) * (b//(2*(1<<i)))
        t = (b+1)%(2*(1<<i))
        if t>0:
            if t > (1<<i):
                sb += t - (1<<i)
        # print(i,sa,sb,((sb-sa)%2)<<i)
        res += ((sb-sa)%2)<<i
    return res


if __name__ == '__main__':
    a,b = map(int, input().split())
    print(f(a,b))
