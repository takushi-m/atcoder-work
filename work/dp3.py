# -*- coding: utf-8 -*-
import unittest

def func(ary, a):
    n = len(ary)
    dp = [[False for _ in range(a+1)] for _ in range(n+1)]
    dp[0][0] = True

    for i in range(n):
        for ai in range(a+1):
            if ai>=ary[i]:
                dp[i+1][ai] = dp[i][ai] or dp[i][ai-ary[i]]
            else:
                dp[i+1][ai] = dp[i][ai]

    if dp[n][a]:
        return "YES"
    else:
        return "NO"

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(func([7,5,3], 10), "YES")
        self.assertEqual(func([9,7], 6), "NO")

if __name__ == '__main__':
    unittest.main()
