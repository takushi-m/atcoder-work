# -*- coding: utf-8 -*-
import unittest

def func(load, W):
    n = len(load)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n):
        for w in range(W+1):
            if load[i][0]<=w:
                dp[i+1][w] = max(dp[i][w], dp[i][w-load[i][0]]+load[i][1])
            else:
                dp[i+1][w] = dp[i][w]
    return dp[n][W]

class Test(unittest.TestCase):
    def test(self):
        load = [
            [2,3] # [w, v]
            ,[1,2]
            ,[3,4]
            ,[2,2]
        ]
        self.assertEqual(func(load, 5), 7)

if __name__ == '__main__':
    unittest.main()
