# -*- coding: utf-8 -*-
import unittest

maxv = 100*100
inf = 10**8

def func(load, W):
    n = len(load)
    dp = [[inf for _ in range(maxv+1)] for _ in range(n+1)]
    # dp[i+1][j] i番目まで選んで価値をjにした時の最小の重さ
    dp[0][0] = 0
    for i in range(n):
        for j in range(maxv+1):
            if load[i][1]<=j:
                dp[i+1][j] = min(
                    dp[i][j]
                    ,dp[i][j-load[i][1]] + load[i][0]
                )
            else:
                dp[i+1][j] = dp[i][j]
    ret = 0
    for v in range(maxv):
        if dp[n][v]<=W:
            ret = max(ret, v)
    return ret

class Test(unittest.TestCase):
    def test(self):
        load = [
            [2,3] # [w,v]
            ,[1,2]
            ,[3,4]
            ,[2,2]
        ]
        self.assertEqual(func(load, 5), 7)

if __name__ == '__main__':
    unittest.main()
