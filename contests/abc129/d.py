# -*- coding: utf-8 -*-

def f(h,w,sl):
    cnt = [[[0,0] for _ in range(w)] for _ in range(h)]

    for hi in range(h):
        wi = 0
        while wi<w:
            if sl[hi][wi]==".":
                c = 0
                wj = wi
                while wj<w and sl[hi][wj]==".":
                    c += 1
                    wj += 1
                for j in range(wi,wj):
                    cnt[hi][j][0] = c
                wi = wj
            else:
                wi += 1

    for wi in range(h):
        hi = 0
        while hi<h:
            if sl[hi][wi]==".":
                c = 0
                hj = hi
                while hj<h and sl[hj][wi]==".":
                    c += 1
                    hj += 1
                for j in range(hi,hj):
                    cnt[j][wi][1] = c
                hi = hj
            else:
                hi += 1

    res = -1
    for hi in range(h):
        for wi in range(w):
            if sl[hi][wi]==".":
                r = sum(cnt[hi][wi])
                res = max(res, r)

    return res-1


if __name__ == '__main__':
    h,w = map(int, input().split())
    sl = [input() for _ in range(h)]
    print(f(h,w,sl))

    # from random import choice
    # for _ in range(1):
    #     h = 2000
    #     w = 2000
    #     sl = ["".join([choice([".","#"]) for _ in range(w)]) for _ in range(h)]
