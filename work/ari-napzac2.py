# -*- coding: utf-8 -*-
import unittest

def func(load, W):
    n = len(load)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n):
        for w in range(W+1):
            if load[i][0]<=w:
                dp[i+1][w] = max(
                    dp[i][w]
                    ,dp[i+1][w-load[i][0]]+load[i][1]
                )
            else:
                dp[i+1][w] = dp[i][w]
    return dp[n][W]

class Test(unittest.TestCase):
    def test(self):
        load = [
            [3,4] # [w,v]
            ,[4,5]
            ,[2,3]
        ]
        self.assertEqual(func(load, 7), 10)

if __name__ == '__main__':
    unittest.main()
