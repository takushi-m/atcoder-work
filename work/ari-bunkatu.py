# -*- coding: utf-8 -*-
import unittest

MOD = 1000

def func(n,m):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 1
    for i in range(1,m+1):
        for j in range(n+1):
            if j-i>=0:
                dp[i][j] = (dp[i][j-i] + dp[i-1][j])%MOD
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func(4,3), 4)

if __name__ == '__main__':
    unittest.main()
