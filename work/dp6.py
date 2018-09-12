# -*- coding: utf-8 -*-
import unittest

inf = 10**8

def func(ary, a, k):
    n = len(ary)
    dp = [[inf for _ in range(a+1)] for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for ai in range(a+1):
            if ai>=ary[i]:
                dp[i+1][ai] = min(dp[i][ai], dp[i][ai-ary[i]]+1)
            else:
                dp[i+1][ai] = dp[i+1][ai]
    if k>=dp[n][a]>0:
        return dp[n][a]
    else:
        return -1

class Test(unittest.TestCase):
    def func(self):
        self.assertEqual(func([7,5,3], 10, 2), "YES")
        self.assertEqual(func([7,5,3], 10, 1), "NO")

if __name__ == '__main__':
    unittest.main()
