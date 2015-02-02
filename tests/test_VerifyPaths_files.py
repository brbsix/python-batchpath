#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import VerifyPaths
import os
import unittest

class VerifyPathsFilesTestCase(unittest.TestCase):
    def test_paths_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths)
        self.assertTrue(status)

    def test_paths_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths)
        self.assertFalse(status)

    def test_access_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, access=os.W_OK)
        self.assertTrue(status)

    def test_access_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, access=os.W_OK)
        self.assertFalse(status)

    def test_extensions_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, extensions=[])
        self.assertTrue(status)

    def test_extensions_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, extensions=[])
        self.assertFalse(status)

    def test_minsize_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, minsize=0)
        self.assertTrue(status)

    def test_minsize_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, minsize=0)
        self.assertFalse(status)

    def test_all_options_true(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, os.W_OK, [], 0)
        self.assertTrue(status)

    def test_all_options_false(self):
        paths = []

        vp = VerifyPaths()
        status = vp.files(paths, os.W_OK, [], 0)
        self.assertFalse(status)

if __name__ == '__main__':
    unittest.main()
