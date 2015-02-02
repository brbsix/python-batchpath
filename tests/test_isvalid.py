#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import isvalid
import os
import unittest


class IsValidTestCase(unittest.TestCase):
    def test_exists_true(self):
        path = 'content/.DirectoryA/SubdirA/emptyfileA'
        status = isvalid(path, filetype='any')
        self.assertTrue(status)

    def test_exists_false(self):
        path = 'content/fail.txt'
        status = isvalid(path, filetype='any')
        self.assertFalse(status)

    def test_access_true(self):
        path = 'content/.DirectoryA/SubdirB/nonemptyA'
        status = isvalid(path, access=os.W_OK)
        self.assertTrue(status)

    def test_access_false(self):
        path = 'content/.DirectoryA/SubdirB/nonempty_rootA'
        status = isvalid(path, access=os.W_OK)
        self.assertFalse(status)

    def test_extensions_single_true(self):
        path = 'content/file1.txt'
        status = isvalid(path, extensions=['txt'])
        self.assertTrue(status)

    def test_extensions_single_false(self):
        path = 'content/file1.txt'
        status = isvalid(path, extensions=['jpg'])
        self.assertFalse(status)

    def test_extensions_multiple_true(self):
        path = 'content/file1.txt'
        status = isvalid(path, extensions=['asc', 'bmp', 'jpg', 'txt', 'zip'])
        self.assertTrue(status)

    def test_extensions_multiple_false(self):
        path = 'content/file1.txt'
        status = isvalid(path, extensions=['asc', 'bmp', 'jpg', 'zip'])
        self.assertFalse(status)

    def test_filetype_file_true(self):
        path = 'content/DirectoryD\\n/SubdirB/emptyA'
        status = isvalid(path, filetype='file')
        self.assertTrue(status)

    def test_filetype_file_false(self):
        path = 'content/DirectoryD\\n/SubdirB'
        status = isvalid(path, filetype='file')
        self.assertFalse(status)

    def test_filetype_dir_true(self):
        path = 'content/DirectoryD\\n'
        status = isvalid(path, filetype='dir')
        self.assertTrue(status)

    def test_filetype_dir_false(self):
        path = 'content/DirectoryD\\n/SubdirB/emptyB'
        status = isvalid(path, filetype='dir')
        self.assertFalse(status)

    def test_minsize_zero_true(self):
        path = 'content/DirectoryE/SubdirA/nonemptyC'
        status = isvalid(path, minsize=0)
        self.assertTrue(status)

    def test_minsize_zero_false(self):
        path = 'content/DirectoryE/SubdirB/empty_rootB'
        status = isvalid(path, minsize=0)
        self.assertFalse(status)

    def test_all_options_true(self):
        path = 'content/file2_nonempty.txt'
        status = isvalid(path, os.W_OK, ['gif', 'txt', 'zip'], 'file', 0)
        self.assertTrue(status)

    def test_all_options_false(self):
        path = 'content/DirectoryE/SubdirB/empty_rootC'
        status = isvalid(path, os.W_OK, ['pub', 'txt'], 'dir', 0)
        self.assertFalse(status)

if __name__ == '__main__':
    unittest.main()
