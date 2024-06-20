"""Module for performing unit-tests on my functions"""

import unittest
from maximum_depth_of_binary_tree import Solution
from maximum_depth_of_binary_tree_2 import Solution as Solution2
from test_cases import TestCases

# pylint: disable=W0622


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 2

    def which_method_to_test(self, which, x) -> int:
        """Decide which variation method to test"""
        s = Solution()
        t = Solution2()
        if which == 1:
            return s.max_depth_1(x)
        elif which == 2:
            return t.max_depth_2(x)

    def test_depth_of_3(self):
        """Testing binary tree depth of 3"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, TestCases.test_1_head)
            self.assertEqual(
                result,
                TestCases.solution_1,
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on binary tree depth of 3.",
            )

    def test_depth_of_2(self):
        """Testing binary tree depth of 2"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, TestCases.test_2_head)
            self.assertEqual(
                result,
                TestCases.solution_2,
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on binary tree depth of 2.",
            )

    def test_depth_of_1(self):
        """Testing binary tree depth of 1"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, TestCases.test_3_head)
            self.assertEqual(
                result,
                TestCases.solution_3,
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on binary tree depth of 1.",
            )

    def test_depth_of_0(self):
        """Testing binary tree depth of 0"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, TestCases.test_4_head)
            self.assertEqual(
                result,
                TestCases.solution_4,
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on binary tree depth of 0.",
            )


if __name__ == "__main__":
    unittest.main()
