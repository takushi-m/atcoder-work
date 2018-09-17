# -*- coding: utf-8 -*-
import unittest

def func(m,n,c):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for mi in range(m):
        for ni in range(n):
            dp[mi+1][ni+1] = max(
                dp[mi][ni]
                ,dp[mi+1][ni]
                ,dp[mi][ni+1]
            ) + c[mi][ni]
    return dp[m][n]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func(2,3,[[1,1,1], [2,2,2]]), 7)

if __name__ == '__main__':
    unittest.main()
