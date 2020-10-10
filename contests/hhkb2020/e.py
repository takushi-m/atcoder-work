from functools import lru_cache

h,w = map(int, input().split())
s = [input() for _ in range(h)]
mod = 10**9 + 7

k = 0
for hi in range(h):
    k += s[hi].count(".")

light = [[-1]*w for _ in range(h)]
for hi in range(h):
    wi = 0
    while wi<w:
        if s[hi][wi]==".":
            ww = s[hi].find("#", wi)
            if ww<0:
                ww = w
            c = ww - wi
            for i in range(wi,ww):
                light[hi][i] += c
            wi = ww
        else:
            wi += 1
for wi in range(w):
    hi = 0
    while hi<h:
        if s[hi][wi]==".":
            hh = hi
            while hh<h and s[hh][wi]==".":
                hh += 1
            c = hh - hi
            for i in range(hi,hh):
                light[i][wi] += c
            hi = hh
        else:
            hi += 1

@lru_cache(maxsize=h*w)
def calc(l):
    r = (pow(2,l,mod) + mod - 1)%mod
    r = r * pow(2,k-l,mod)
    r %= mod
    return r


ans = 0
for hi in range(h):
    for wi in range(w):
        if s[hi][wi]==".":
            ans += calc(light[hi][wi])
print(ans%mod)
