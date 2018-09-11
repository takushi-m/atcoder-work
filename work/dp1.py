# -*- coding: utf-8 -*-
import unittest

def func(a):
    n = len(a)
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        dp[i+1] = max(dp[i],dp[i]+a[i])
    return dp[n]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(func([7,-6,9]), 16)
        self.assertEqual(func([-8,-7]), 0)
        self.assertEqual(func([1,2]), 3)

if __name__ == '__main__':
    unittest.main()
