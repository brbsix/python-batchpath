#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import VerifyPaths
import os
import unittest

class VerifyPathsAllTestCase(unittest.TestCase):
    def test_paths_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.all(paths)
        self.assertTrue(status)

    def test_paths_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.all(paths)
        self.assertFalse(status)

    def test_access_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.all(paths, access=os.W_OK)
        self.assertTrue(status)

    def test_access_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.all(paths, access=os.W_OK)
        self.assertFalse(status)


if __name__ == '__main__':
    unittest.main()
