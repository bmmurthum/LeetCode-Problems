"""Module for performing unit-tests on my functions"""

import unittest
from path_sum import Solution
from path_sum_2 import Solution as Solution2
from path_sum_3 import Solution as Solution3
from test_cases import TestCases


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 3

    def which_method_to_test(self, which, x, y) -> int:
        """Decide which variation method to test"""
        s = Solution()
        t = Solution2()
        u = Solution3()
        if which == 1:
            return s.has_path_sum_1(x, y)
        elif which == 2:
            return t.has_path_sum_2(x, y)
        elif which == 3:
            return u.has_path_sum_3(x, y)

    def test_target_not_found(self):
        """Testing target not in any path"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_1[0], TestCases.test_1[1]
            )
            self.assertEqual(
                result,
                TestCases.test_1[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. On target not found.",
            )

    def test_one_node_bottom_depth(self):
        """Testing one node on bottom depth"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_2[0], TestCases.test_2[1]
            )
            self.assertEqual(
                result,
                TestCases.test_2[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. One node on bottom depth.",
            )

    def test_full_tree_two_solutions(self):
        """Testing a full tree, with two paths that return true"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_3[0], TestCases.test_3[1]
            )
            self.assertEqual(
                result,
                TestCases.test_3[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. Full tree with two paths that return true.",
            )

    def test_only_left_children(self):
        """Testing only left children"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_4[0], TestCases.test_4[1]
            )
            self.assertEqual(
                result,
                TestCases.test_4[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. Only left children.",
            )

    def test_only_right_children(self):
        """Testing only right children. Also negative total sum."""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_5[0], TestCases.test_5[1]
            )
            self.assertEqual(
                result,
                TestCases.test_5[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. Only right children. Negative total sum.",
            )

    def test_single_node(self):
        """Testing single node"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_6[0], TestCases.test_6[1]
            )
            self.assertEqual(
                result,
                TestCases.test_6[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. Single node.",
            )

    def test_two_nodes(self):
        """Testing two nodes. A node with a negative value."""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_7[0], TestCases.test_7[1]
            )
            self.assertEqual(
                result,
                TestCases.test_7[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. Two nodes.",
            )

    def test_all_zeroes(self):
        """Testing all node values are zero."""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_8[0], TestCases.test_8[1]
            )
            self.assertEqual(
                result,
                TestCases.test_8[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. All zeroes.",
            )

    def test_empty_list(self):
        """Testing empty node tree."""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_9[0], TestCases.test_9[1]
            )
            self.assertEqual(
                result,
                TestCases.test_9[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect. All zeroes.",
            )


if __name__ == "__main__":
    unittest.main()
