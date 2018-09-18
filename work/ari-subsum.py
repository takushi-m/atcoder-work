# -*- coding: utf-8 -*-
import unittest

def func(a, k):
    n = len(a)
    dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(k+1):
            if dp[i][j]>=0:
                dp[i+1][j] = a[i][1]
            elif a[i][0]>j or dp[i+1][j-a[i][0]]<0:
                dp[i+1][j] = -1
            else:
                dp[i+1][j] = dp[i+1][j-a[i][0]]-1
    if dp[n][k]>0:
        return "YES"
    else:
        return "NO"

class Test(unittest.TestCase):
    def test(self):
        a = [
            [3,3]
            ,[5,2] # 5が2個
            ,[8,2]
        ]
        self.assertEqual(func(a, 17), "YES")

if __name__ == '__main__':
    unittest.main()
