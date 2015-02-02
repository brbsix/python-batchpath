#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import checkext
import unittest


class CheckExtTestCase(unittest.TestCase):
    def test_single_extension_true(self):
        status = checkext('/path/to/file.txt', ['txt'])
        self.assertTrue(status)

    def test_single_extension_hidden_file_true(self):
        status = checkext('/path/to/.file.txt', ['txt'])
        self.assertTrue(status)

    def test_multiple_extensions_true(self):
        status = checkext('/path/to/file.txt', ['asc', 'conf', 'mp3', 'txt', 'tz'])
        self.assertTrue(status)

    def test_single_extension_false(self):
        status = checkext('/path/to/file.jpg', ['txt'])
        self.assertFalse(status)

    def test_single_extension_hidden_file_false(self):
        status = checkext('/path/to/.file.jpg', ['txt'])
        self.assertFalse(status)

    def test_multiple_extensions_false(self):
        status = checkext('/path/to/file.jpg', ['asc', 'conf', 'mp3', 'txt', 'tz'])
        self.assertFalse(status)

    def test_no_path_extension(self):
        status = checkext('/path/to/txt', ['txt'])
        self.assertFalse(status)

    def test_no_valid_extensions(self):
        status = checkext('/path/to/file.txt', [])
        self.assertFalse(status)

if __name__ == '__main__':
    unittest.main()
