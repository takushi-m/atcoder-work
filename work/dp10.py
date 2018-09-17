# -*- coding: utf-8 -*-
import unittest

def func(s,t):
    inf = 10**9
    ns = len(s)
    nt = len(t)
    dp = [[inf for _ in range(nt+1)] for _ in range(ns+1)]
    dp[0][0] = 0
    for i in range(ns):
        for j in range(nt):
            # 変更
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = dp[i][j]+1
            # 削除
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1]+1)
            # 追加
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j]+1)
    return dp[ns][nt]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func("abc", "addc"), 2)
        self.assertEqual(func("pirikapirirara", "poporinapeperuto"), 10)

if __name__ == '__main__':
    unittest.main()
