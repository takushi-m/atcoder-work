# -*- coding: utf-8 -*-
import unittest

def func(s,t):
    if s==t:
        return "Yes"
    elif len(size(s))>len(size(t)):
        return "No"

    


    pass

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(func("azzel", "apple"), "Yes")
        self.assertEqual(func("chokudai", "redcoder"), "No")
        self.assertEqual(func("abcdefghijklmnopqrstuvwxyz", "ibyhqfrekavclxjstdwgpzmonu"), "Yes")
        self.assertEqual(func("abc", "abc"), "Yes")

if __name__ == '__main__':
    # s = input()
    # t = input()
    unittest.main()
