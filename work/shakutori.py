# -*- coding: utf-8 -*-
import unittest

"""
int right = 0;
for (int left = 0; left < n; ++left) {
    while (right < n && (right を 1 個進めたときに条件を満たす)) {
        /* 実際に right を 1 進める */
        // ex: sum += a[right];
        ++right;
    }

    /* break した状態で right は条件を満たす最大なので、何かする */
    // ex: res += (right - left);

    /* left をインクリメントする準備 */
    // ex: if (right == left) ++right;
    // ex: else sum -= a[left];
}
"""

class Test1(unittest.TestCase):
    # AOJ Course The Number of Windows
    def f(self,n,x,al):
        res = 0
        for l in range(n):
            for r in range(l+1,n+1):
                if sum(al[l:r])<=x:
                    res += 1
        return res

    def f2(self,n,x,al):
        res = 0
        r = 0
        s = 0
        for l in range(n):
            while r<n and s+al[r]<=x:
                s += al[r]
                r += 1
            res += (r-l)
            if r==l:
                r += 1
            else:
                s -= al[l]
        return res

    def test(self):
        n = 6
        x = 12
        al = [5,3,8,6,1,4]
        self.assertEqual(self.f(n,x,al), 11)
        self.assertEqual(self.f2(n,x,al), 11)


class Test2(unittest.TestCase):
    # POJ 3061 Subsequence
    def f(self,n,x,al):
        res = n+1
        for l in range(n):
            for r in range(l+1,n+1):
                if sum(al[l:r])>=x:
                    res = min(res, r-l)
        return res

    def f2(self,n,x,al):
        res = n+1
        r = 0
        s = 0
        for l in range(n):
            while r<n and s<x:
                s += al[r]
                r += 1
            if s<x:
                break
            res = min(res, r-l)
            if r==l:
                r += 1
            else:
                s -= al[l]
        if res==n+1:
            return 0
        else:
            return res

    def test(self):
        n = 10
        x = 28
        al = [5,1,2,5,10,7,4,9,2,8]
        self.assertEqual(self.f(n,x,al), 4)
        self.assertEqual(self.f2(n,x,al), 4)


import functools
import operator
class Test3(unittest.TestCase):
    # ABC 032 C 列
    def f(self,n,k,al):
        res = 0
        for l in range(n):
            for r in range(l+1,n+1):
                if functools.reduce(operator.mul, al[l:r], 1)<=k:
                    res = max(res, r-l)
        return res

    def f2(self,n,k,al):
        res = 0
        r = 0
        m = 1
        for l in range(n):
            while r<n and m*al[r]<=k:
                m *= al[r]
                r += 1

            res = max(res, r-l)

            if r==l:
                r += 1
            else:
                m //= al[l]
        return res

    def test(self):
        n = 7
        k = 6
        al = [4,3,1,1,2,10,2]
        self.assertEqual(self.f(n,k,al), 4)
        self.assertEqual(self.f2(n,k,al), 4)


class Test4(unittest.TestCase):
    # ABC 038 C 単調増加
    def check(self,l):
        if len(l)==1:
            return True
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:
                return False
        return True

    def f(self,n,al):
        res = 0
        for l in range(n):
            for r in range(l+1,n+1):
                if self.check(al[l:r]):
                    res += 1
        return res

    def f2(self,n,al):
        res = 0
        r = 1
        for l in range(n):
            while r<n and (r==l or al[r-1]<al[r]):
                r += 1

            res += r-l

            if r==l:
                r += 1
        return res

    def test(self):
        n = 5
        al = [1,2,3,2,1]
        self.assertEqual(self.f(n,al), 8)
        self.assertEqual(self.f2(n,al), 8)


class Test5(unittest.TestCase):
    # ARC 022 B 細長いお菓子
    def f(self,n,al):
        res = 0
        for l in range(n):
            for r in range(l+1,n+1):
                if r-l == len(set(al[l:r])):
                    res = max(res, r-l)
        return res

    def f2(self,n,al):
        res = 0
        r = 0
        s = set()
        for l in range(n):
            while r<n and al[r] not in s:
                s.add(al[r])
                r += 1

            res = max(res, r-l)

            if r==l:
                r += 1
            else:
                s.remove(al[l])
        return res

    def test(self):
        n = 7
        al = [1,2,1,3,1,4,4]
        self.assertEqual(self.f(n,al), 3)
        self.assertEqual(self.f2(n,al), 3)


class Test7(unittest.TestCase):
    # ABC 017 D サプリメント
    def f(self,n,m,fl):
        L = [0]*(n+1)
        s = set()
        r = 0
        for l in range(n):
            while r<n and fl[r] not in s:
                s.add(fl[r])
                r += 1
            L[r] = l
            if r==l:
                r += 1
            else:
                s.remove(fl[l])
        print(L)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            dp[i] = sum(dp[L[i]:i])

        return dp[n]

    def test(self):
        n = 5
        m = 2
        fl = [1,2,1,2,2]
        self.assertEqual(self.f(n,m,fl), 5)

if __name__ == '__main__':
    unittest.main()
