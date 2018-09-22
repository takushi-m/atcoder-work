# -*- coding: utf-8 -*-
import unittest

MOD = 10**9 + 7

def func(s):
    abc = "ABC"
    n = len(s)
    dp =[[0 for _ in range(3+1)] for _ in range(n+1)]
    dp[n][3] = 1

    for i in range(n-1,-1,-1):
        for j in range(3,-1,-1):
            if j==3:
                if s[i]=="?":
                    dp[i][j] = (dp[i+1][j]*3)%MOD
                else:
                    dp[i][j] = dp[i+1][j]
            else:
                m1 = 3 if s[i]=="?" else 1
                m2 = 1 if s[i]=="?" or s[i]==abc[j] else 0
                dp[i][j] = ((m1*dp[i+1][j])%MOD + (m2*dp[i+1][j+1])%MOD)%MOD
    return dp[0][0]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func("A??C"), 8)
        self.assertEqual(func("ABCBC"), 3)
        self.assertEqual(func("????C?????B??????A???????"), 979596887
)

if __name__ == '__main__':
    print(func(input()))
