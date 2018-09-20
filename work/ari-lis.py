# -*- coding: utf-8 -*-
import unittest

def func(a):
    n = len(a)
    dp = [1 for _ in range(n)]
    ret = -1
    for i in range(n):
        for j in range(i):
            if a[j]<a[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ret = max(ret, dp[i])
    return ret

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func([1,2,3]), 3)
        self.assertEqual(func([4,2,3,1,5]), 3)

if __name__ == '__main__':
    unittest.main()
