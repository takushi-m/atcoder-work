# -*- coding: utf-8 -*-
import unittest

def func(T, g):
    dp = [0 for _ in range(T+2)]

    for t in range(T+1):
        for i in range(t):
            for j in range(i+1,t+1):
                dp[t+1] = max(dp[t+1], dp[i]+g[i][j-1])
    return dp[T+1]

class Test(unittest.TestCase):
    def test(self):
        g = [
            [3,7,4,8]
            ,[0,5,9,7]
            ,[0,0,8,5]
            ,[0,0,0,6]
        ]
        self.assertEqual(func(4, g), 13)

if __name__ == '__main__':
    unittest.main()
