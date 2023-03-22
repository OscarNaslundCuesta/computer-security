#!/usr/bin/env python3

import unittest

import antivirus
import malware

class test(unittest.TestCase):
    def testNoMalware1(self):
        self.assertIsNone(antivirus.check("antivirus.py"))
    def testIsMalware1(self):
        self.assertIs(antivirus.check("payload1.py"), 1)
    def testIsMalware2(self):
        self.assertIs(antivirus.check("payload2.py"), 2)
    def testEncrypted(self):
        malware.inject("antivirus.py", "antivirus.py", "result.py")
        self.assertIsNone(antivirus.check("result.py"))
    def testEncrypted1(self):
        malware.inject("antivirus.py", "payload1.py", "result.py")
        self.assertIs(antivirus.check("result.py"), 1)
    def testEncrypted2(self):
        malware.inject("antivirus.py", "payload2.py", "result.py")
        self.assertIs(antivirus.check("result.py"), 2)


if __name__ == '__main__':
    unittest.main()
