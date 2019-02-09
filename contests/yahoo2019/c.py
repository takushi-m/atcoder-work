# -*- coding: utf-8 -*-

def f(k,a,b):
    if b-a<=0:
        return k+1
    elif k+1<a:
        return k+1
    else:
        res1 = k+1
        res2 = b
        k -= 1+a
        # print(k,res2)
        if k>0:
            res2 += (b-a)*(k//2)
            res2 += k%2
        elif k<0:
            res2 = -1
        return max(res1, res2)

def f2(k,a,b):
    k_ = k
    res = 1
    while k>0 and res<a:
        res += 1
        k -= 1
    res += (b-a)*(k//2)
    res += k%2
    return max(res, k_+1)

if __name__ == '__main__':
    k,a,b = map(int, input().split())
    print(f(k,a,b))

    # print(f(3,3,5))
    # from random import randint
    # for _ in range(1000):
    #     k = randint(1,100)
    #     a = randint(1,100)
    #     b = randint(1,100)
    #     res1 = f(k,a,b)
    #     res2 = f2(k,a,b)
    #     if res1!=res2:
    #         print(k,a,b)
    #         print(res1,res2)
    #         break
