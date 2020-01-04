# coding: utf-8
import sys
import unittest
from io import StringIO

import timeout_decorator

import _ as task


class AtCoderTestCase(unittest.TestCase):

    examples = [
        # SAMPLES
    ]

    boundaries = [
    ]

    @timeout_decorator.timeout(2)
    def test_examples(self):
        for i, o in self.examples:
            with self.subTest(i=i, o=o):
                self.assertEqual(task.solve(
                    *(i if isinstance(i, tuple) else (i,))
                ), o)

    @timeout_decorator.timeout(2)
    def test_boundaries(self):
        for i, o in self.boundaries:
            with self.subTest(i=i, o=o):
                self.assertEqual(task.solve(
                    *(i if isinstance(i, tuple) else (i,))
                ), o)

    def setUp(self):
        sys.stdout = self.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        out = self.stdout.getvalue()
        print(out)
        with self.subTest():
            self.assertEqual(len(out), 0,
                             msg='Remove print command')


if __name__ == "__main__":
    unittest.main()
