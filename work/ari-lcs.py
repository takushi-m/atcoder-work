# -*- coding: utf-8 -*-
import unittest

def func(s,t):
    ns = len(s)
    nt = len(t)
    dp = [[0 for _ in range(nt+1)] for _ in range(ns+1)]

    for i in range(ns):
        for j in range(nt):
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
    return dp[ns][nt]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func("abcd", "becd"), 3)

if __name__ == '__main__':
    unittest.main()
