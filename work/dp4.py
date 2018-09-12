# -*- coding: utf-8 -*-
import unittest

MOD = 1000000009

def func(ary, a):
    n = len(ary)
    dp = [[0 for _ in range(a+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for ai in range(a+1):
            if ai>=ary[i]:
                dp[i+1][ai] = dp[i][ai] + dp[i][ai-ary[i]]
            else:
                dp[i+1][ai] = dp[i][ai]
    return dp[n][a]%MOD

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(func([7,5,3,1,8], 12), 2)
        self.assertEqual(func([4,1,1,1], 5), 3)

if __name__ == '__main__':
    unittest.main()
