#!/usr/bin/env python3

from crypto import *
from sec_crypto import *
from crypto_old import *

import unittest
import random

class test(unittest.TestCase):
    def side_channel(self, v1, v2, k1, k2):
        c1 = Cache()
        e1 = SecCrypto()
        e1.load_table(c1)
        c2 = Cache()
        e2 = SecCrypto()
        e2.load_table(c2)

        for l in range(cache_lines):
            c1.read_address(l*cache_line_size+cache_lines*cache_line_size)
            c2.read_address(l*cache_line_size+cache_lines*cache_line_size)
            
        v1 = e1.feistel_encrypt(c1, v1, k1)
        v2 = e2.feistel_encrypt(c2, v2, k2)
        self.assertEqual(c1.cache, c2.cache)
        
    def test1(self):
        self.side_channel("ab", "cd", "x1", "y1")
    def test2(self):
        for x in range(100):
            strings = [chr(random.randint(0,255)) + chr(random.randint(0,255)) for i in range(4)]
            self.side_channel(strings[0], strings[1], strings[2], strings[3])

    def verify_crypto(self, v1, k1):
        c1 = Cache()
        e1 = Crypto()
        e1.load_table(c1)
        c2 = Cache()
        e2 = SecCrypto()
        e2.load_table(c2)

        c3 = Cache()
        e3 = CryptoOld()

        r1 = e1.feistel_encrypt(c1, v1, k1)
        r2 = e2.feistel_encrypt(c2, v1, k1)
        r3 = e3.feistel_encrypt(c2, v1, k1)
        self.assertTrue((r1 == r2) or (r3 == r2))

    def test3(self):
        self.verify_crypto("ab",  "x1")
    def test4(self):
        for x in range(100):
            strings = [chr(random.randint(0,255)) + chr(random.randint(0,255)) for i in range(2)]
            self.verify_crypto(strings[0], strings[1])

if __name__ == '__main__':
    unittest.main()
