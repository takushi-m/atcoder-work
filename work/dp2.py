# -*- coding: utf-8 -*-
import unittest

def func(ary_wv, W):
    n = len(ary_wv)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for wi in range(W+1):
        dp[0][wi] = 0

    for wi in range(1, W+1):
        for i in range(n):
            if ary_wv[i][0]>wi:
                dp[i+1][wi] = dp[i][wi]
            else:
                dp[i+1][wi] = max(dp[i][wi], dp[i][wi-ary_wv[i][0]]+ary_wv[i][1])

    return dp[n][W]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(func([
            [2,3] # [w, v]
            ,[1,2]
            ,[3,6]
            ,[2,1]
            ,[1,3]
            ,[5,85]
        ], 8), 91)

if __name__ == '__main__':
    unittest.main()
