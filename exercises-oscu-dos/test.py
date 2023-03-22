#!/usr/bin/env python3

import unittest

import filter


class test(unittest.TestCase):
    def testNoBadInput(self):
        self.assertTrue(filter.filter_text("""
# ab = hello
# cd = test
I'm a text
"""))

    def testBadInput(self):
        self.assertFalse(filter.filter_text("""
# a = hellbo
# b = testc
# c = an
I'm a text
"""))


if __name__ == '__main__':
    unittest.main()
