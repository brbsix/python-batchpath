#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import GeneratePaths
import os
import unittest


class GeneratePathDirsTestCase(unittest.TestCase):
    def test_nonrecursive(self):
        paths = ['content']
        basenames = ['content/-DirectoryB',
                     'content/.DirectoryA',
                     'content/DirectoryD\\n',
                     'content/DirectoryE',
                     'content/DirectoryF',
                     'content/\\nDirectoryC']


        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.dirs(paths)

        self.assertEqual(output, expected)

    def test_recursion(self):
        paths = ['content']
        basenames = ['content/-DirectoryB',
                     'content/.DirectoryA',
                     'content/DirectoryD\\n',
                     'content/DirectoryE',
                     'content/DirectoryF',
                     'content/\\nDirectoryC',
                     'content/.DirectoryA/SubdirA',
                     'content/.DirectoryA/SubdirB',
                     'content/.DirectoryA/SubdirC',
                     'content/DirectoryD\\n/SubdirA',
                     'content/DirectoryD\\n/SubdirB',
                     'content/DirectoryD\\n/SubdirC',
                     'content/DirectoryE/SubdirA',
                     'content/DirectoryE/SubdirB',
                     'content/DirectoryE/SubdirC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.dirs(paths, recursion=True)

        self.assertEqual(output, expected)

    def test_access_recursion(self):
        paths = ['content/DirectoryD\\n', 'content/DirectoryE']
        basenames = ['content/DirectoryE/SubdirA',
                    'content/DirectoryE/SubdirB',
                    'content/DirectoryE/SubdirC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.dirs(paths, access=os.W_OK, recursion=True)

        self.assertEqual(output, expected)

    def test_filter_invalid_paths(self):
        paths = ['content/.DirectoryA', 'content/does_not_exist',
                 'content/does_not_exist/subdirectory']
        basenames = ['content/.DirectoryA/SubdirA',
                     'content/.DirectoryA/SubdirB',
                     'content/.DirectoryA/SubdirC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.dirs(paths)

        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
