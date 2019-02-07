# -*- coding: utf-8 -*-
# 平方分割練習
# https://www.slideshare.net/iwiwi/ss-3578491

from random import randint

n = 1000000
al = [randint(0,1000) for _ in range(n)]

ql = [
    (0,1000000),
    (50000,90000),
    (10,20),
    (999990,1000000)
]

def f(a,b):
    # 愚直な方法 O(n)
    return min(al[a:b])

# sqrt(n)分割して、その区間での最小値を取っておく。構築にO(n)
size = 1000 # 最大のnに対してsqrtをとった数で計算
bl = []
for i in range(size):
    # [i*b,i*b+b)の範囲での最小値を取っておく
    bmin = min(al[i*size:i*size+size])
    bl.append(bmin)


def f2(a,b):
    ia = a//size
    ib = b//size

    if ib-ia<2:
        # 両端が重なっていたり、隣り合っている場合は愚直にやる
        # 区間の幅が最大で2*sqrt(n)なので、O(sqrt(n))
        return min(al[a:b])

    l = [
        # 両端の区間は愚直に
        min(al[a:ia*size+size]), # O(sqrt(n))
        min(al[ib*size-1:b]), # O(sqrt(n))
        # 間の区間たちは事前に構築したデータから計算できる
        min(bl[ia+1:ib]) # O(sqrt(n))
    ]
    return min(l)

for a,b in ql:
    print(f(a,b), f2(a,b))
