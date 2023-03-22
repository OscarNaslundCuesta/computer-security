#!/usr/bin/env python3

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
        with open("solution1.txt", "r") as f:
            lines = f.read().split("\n")
        value = [l.split(" ") for l in lines if not(l.startswith("#"))][0]
        res = subprocess.check_output(["./main.elf"] + value)
        self.assertTrue(res.find("pwd0".encode()) >= 0)


if __name__ == '__main__':
    unittest.main()

