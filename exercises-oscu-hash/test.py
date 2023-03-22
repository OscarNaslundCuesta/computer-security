#!/usr/bin/env python3

import unittest
import random
import string

import insecure_hash
import collision


class test(unittest.TestCase):
    def singleTest(self, value):
        value = value.encode()
        print("message %s" % value)
        h = insecure_hash.hash_string(value)
        c = collision.find_collision(value)
        self.assertTrue(c != value) # the function should not return value directly
        h1 = insecure_hash.hash_string(c)
        self.assertTrue(h == h1)

    def test1(self):
        self.singleTest("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb")

    def test2(self):
        self.singleTest("0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF")

    def test3(self):
        self.singleTest("""
Whereas recognition of the inherent dignity and of the equal and inalienable
rights of all members of the human family is the foundation of freedom, justice
and peace in the world
""")

    def test4(self):
        n = random.randint(32, 100)
        message = ''.join([random.choice(string.ascii_letters + " \n") for
                           _ in range(n)])
        self.singleTest(message)


if __name__ == '__main__':
    unittest.main()
