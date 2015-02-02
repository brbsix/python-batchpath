#!/usr/bin/python3
# -*- coding: utf-8 -*-


from batchpath import GeneratePaths
import os
import unittest


class GeneratePathAllTestCase(unittest.TestCase):
    def test_nonrecursive(self):
        paths = ['content']
        basenames = ['content/-DirectoryB',
                     'content/.DirectoryA',
                     'content/DirectoryD\\n',
                     'content/DirectoryE',
                     'content/DirectoryF',
                     'content/\\nDirectoryC',
                     'content/file1.txt',
                     'content/file2_nonempty.txt',
                     'content/file3.conf']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.all(paths)

        self.assertEqual(output, expected)

    def test_recursion(self):
        paths = ['content']
        basenames = ['content/-DirectoryB',
                     'content/.DirectoryA',
                     'content/DirectoryD\\n',
                     'content/DirectoryE',
                     'content/DirectoryF',
                     'content/\\nDirectoryC',
                     'content/file1.txt',
                     'content/file2_nonempty.txt',
                     'content/file3.conf',
                     'content/.DirectoryA/SubdirA',
                     'content/.DirectoryA/SubdirB',
                     'content/.DirectoryA/SubdirC',
                     'content/.DirectoryA/SubdirA/emptyfileA',
                     'content/.DirectoryA/SubdirA/emptyfileB',
                     'content/.DirectoryA/SubdirA/emptyfileC',
                     'content/.DirectoryA/SubdirA/nonemptyA',
                     'content/.DirectoryA/SubdirA/nonemptyB',
                     'content/.DirectoryA/SubdirA/nonemptyC',
                     'content/.DirectoryA/SubdirB/emptyA',
                     'content/.DirectoryA/SubdirB/emptyB',
                     'content/.DirectoryA/SubdirB/emptyC',
                     'content/.DirectoryA/SubdirB/empty_rootA',
                     'content/.DirectoryA/SubdirB/empty_rootB',
                     'content/.DirectoryA/SubdirB/empty_rootC',
                     'content/.DirectoryA/SubdirB/nonemptyA',
                     'content/.DirectoryA/SubdirB/nonemptyB',
                     'content/.DirectoryA/SubdirB/nonemptyC',
                     'content/.DirectoryA/SubdirB/nonempty_rootA',
                     'content/.DirectoryA/SubdirB/nonempty_rootB',
                     'content/.DirectoryA/SubdirB/nonempty_rootC',
                     'content/DirectoryD\\n/SubdirA',
                     'content/DirectoryD\\n/SubdirB',
                     'content/DirectoryD\\n/SubdirC',
                     'content/DirectoryD\\n/SubdirA/emptyfileA',
                     'content/DirectoryD\\n/SubdirA/emptyfileB',
                     'content/DirectoryD\\n/SubdirA/emptyfileC',
                     'content/DirectoryD\\n/SubdirA/nonemptyA',
                     'content/DirectoryD\\n/SubdirA/nonemptyB',
                     'content/DirectoryD\\n/SubdirA/nonemptyC',
                     'content/DirectoryD\\n/SubdirB/emptyA',
                     'content/DirectoryD\\n/SubdirB/emptyB',
                     'content/DirectoryD\\n/SubdirB/emptyC',
                     'content/DirectoryD\\n/SubdirB/empty_rootA',
                     'content/DirectoryD\\n/SubdirB/empty_rootB',
                     'content/DirectoryD\\n/SubdirB/empty_rootC',
                     'content/DirectoryD\\n/SubdirB/nonemptyA',
                     'content/DirectoryD\\n/SubdirB/nonemptyB',
                     'content/DirectoryD\\n/SubdirB/nonemptyC',
                     'content/DirectoryD\\n/SubdirB/nonempty_rootA',
                     'content/DirectoryD\\n/SubdirB/nonempty_rootB',
                     'content/DirectoryD\\n/SubdirB/nonempty_rootC',
                     'content/DirectoryE/SubdirA',
                     'content/DirectoryE/SubdirB',
                     'content/DirectoryE/SubdirC',
                     'content/DirectoryE/SubdirA/emptyfileA',
                     'content/DirectoryE/SubdirA/emptyfileB',
                     'content/DirectoryE/SubdirA/emptyfileC',
                     'content/DirectoryE/SubdirA/nonemptyA',
                     'content/DirectoryE/SubdirA/nonemptyB',
                     'content/DirectoryE/SubdirA/nonemptyC',
                     'content/DirectoryE/SubdirB/emptyA',
                     'content/DirectoryE/SubdirB/emptyB',
                     'content/DirectoryE/SubdirB/emptyC',
                     'content/DirectoryE/SubdirB/empty_rootA',
                     'content/DirectoryE/SubdirB/empty_rootB',
                     'content/DirectoryE/SubdirB/empty_rootC',
                     'content/DirectoryE/SubdirB/nonemptyA',
                     'content/DirectoryE/SubdirB/nonemptyB',
                     'content/DirectoryE/SubdirB/nonemptyC',
                     'content/DirectoryE/SubdirB/nonempty_rootA',
                     'content/DirectoryE/SubdirB/nonempty_rootB',
                     'content/DirectoryE/SubdirB/nonempty_rootC']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.all(paths, recursion=True)

        self.assertEqual(output, expected)

    def test_access_recursion(self):
        paths = ['content/.DirectoryA', 'content/-DirectoryB']
        basenames = ['content/.DirectoryA/SubdirA',
                     'content/.DirectoryA/SubdirB',
                     'content/.DirectoryA/SubdirC',
                     'content/.DirectoryA/SubdirA/emptyfileA',
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
        output = gp.all(paths, access=os.W_OK, recursion=True)

        self.assertEqual(output, expected)

    def test_filter_invalid_paths(self):
        paths = ['content', 'content/does_not_exist', 'content/does_not_exist/subdirectory']
        basenames = ['content/-DirectoryB',
                     'content/.DirectoryA',
                     'content/DirectoryD\\n',
                     'content/DirectoryE',
                     'content/DirectoryF',
                     'content/\\nDirectoryC',
                     'content/file1.txt',
                     'content/file2_nonempty.txt',
                     'content/file3.conf']

        expected = [os.path.abspath(p) for p in basenames]

        gp = GeneratePaths()
        output = gp.all(paths)

        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
