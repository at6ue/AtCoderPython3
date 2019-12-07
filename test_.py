# coding: utf-8
import unittest
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


if __name__ == "__main__":
    unittest.main()
