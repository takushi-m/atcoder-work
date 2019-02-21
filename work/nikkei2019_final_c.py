# -*- coding: utf-8 -*-


def f(h, w, k, rc):
    n = h * w - k
    hl = [w] * h
    wl = [h] * w
    res = 0

    for i in range(k):
        r, c = rc[i]
        hl[r-1] -= 1
        wl[c-1] -= 1

    s = 0
    si = h-1
    for i in range(h):
        s += hl[i]
        if 2 * s >= n:
            si = i
            break
    for i in range(h):
        res += abs(i-si) * hl[i]

    s = 0
    si = w-1
    for i in range(w):
        s += wl[i]
        if 2 * s >= n:
            si = i
            break
    for i in range(w):
        res += abs(i-si) * wl[i]

    return res


if __name__ == '__main__':
    h,w,k = map(int,input().split())
    rc = [list(map(int, input().split())) for _ in range(k)]
    print(f(h,w,k,rc))
