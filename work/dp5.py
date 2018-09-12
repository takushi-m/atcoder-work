# -*- coding: utf-8 -*-
import unittest

inf = 10**8

def func(ary, a):
    n = len(ary)
    dp = [[inf for _ in range(a+1)] for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for ai in range(a+1):
            if ai>=ary[i]:
                dp[i+1][ai] = min(dp[i][ai], dp[i][ai-ary[i]]+1)
            else:
                dp[i+1][ai] = dp[i+1][ai]
    if dp[n][a]>=inf:
        return -1
    else:
        return dp[n][a]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func([7,5,3,1,8], 12), 2)
        self.assertEqual(func([7,5], 6), -1)

if __name__ == '__main__':
    unittest.main()
