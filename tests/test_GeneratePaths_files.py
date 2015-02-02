#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import GeneratePaths
import os
import unittest


class GeneratePathFilesTestCase(unittest.TestCase):
    def test_nonrecursive(self):
        paths = ['content/.DirectoryA/SubdirA', 'content/DirectoryE/SubdirA']
        basenames = ['content/.DirectoryA/SubdirA/emptyfileA',
                     'content/.DirectoryA/SubdirA/emptyfileB',
                     'content/.DirectoryA/SubdirA/emptyfileC',
                     'content/.DirectoryA/SubdirA/nonemptyA',
                     'content/.DirectoryA/SubdirA/nonemptyB',
                     'content/.DirectoryA/SubdirA/nonemptyC',
                     'content/DirectoryE/SubdirA/emptyfileA',
                     'content/DirectoryE/SubdirA/emptyfileB',
                     'content/DirectoryE/SubdirA/emptyfileC',
                     'content/DirectoryE/SubdirA/nonemptyA',
                     'content/DirectoryE/SubdirA/nonemptyB',
                     'content/DirectoryE/SubdirA/nonemptyC']


        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.files(paths)

        self.assertEqual(output, expected)

    def test_minsize_nonrecursive(self):
        paths = ['content/.DirectoryA/SubdirB']
        basenames = ['content/.DirectoryA/SubdirB/nonemptyA',
                     'content/.DirectoryA/SubdirB/nonemptyB',
                     'content/.DirectoryA/SubdirB/nonemptyC',
                     'content/.DirectoryA/SubdirB/nonempty_rootA',
                     'content/.DirectoryA/SubdirB/nonempty_rootB',
                     'content/.DirectoryA/SubdirB/nonempty_rootC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.files(paths, minsize=0)

        self.assertEqual(output, expected)

    def test_access_recursion(self):
        paths = ['content/.DirectoryA']
        basenames = ['content/.DirectoryA/SubdirA/emptyfileA',
                     'content/.DirectoryA/SubdirA/emptyfileB',
                     'content/.DirectoryA/SubdirA/emptyfileC',
                     'content/.DirectoryA/SubdirA/nonemptyA',
                     'content/.DirectoryA/SubdirA/nonemptyB',
                     'content/.DirectoryA/SubdirA/nonemptyC',
                     'content/.DirectoryA/SubdirB/emptyA',
                     'content/.DirectoryA/SubdirB/emptyB',
                     'content/.DirectoryA/SubdirB/emptyC',
                     'content/.DirectoryA/SubdirB/nonemptyA',
                     'content/.DirectoryA/SubdirB/nonemptyB',
                     'content/.DirectoryA/SubdirB/nonemptyC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.files(paths, access=os.W_OK, recursion=True)

        self.assertEqual(output, expected)

    def test_filter_invalid_paths(self):
        paths = ['content/.DirectoryA/SubdirB/emptyA',
                 'content/DirectoryD\\n/SubdirA/nonemptyA',
                 'content/does_not_exist/nonfile',
                 'content/does_not_exist/otherfile']
        basenames = ['content/.DirectoryA/SubdirB/emptyA',
                     'content/DirectoryD\\n/SubdirA/nonemptyA']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.files(paths)

        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
