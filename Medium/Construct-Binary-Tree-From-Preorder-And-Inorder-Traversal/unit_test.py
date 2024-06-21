"""Module for performing unit-tests on my functions"""

import unittest
from construct_binary_tree_from_preorder import Solution
from other_solution import Solution as Solution2
from print_tree_as_list import display_tree_as_list
from test_cases import TestCases

# pylint: disable=W0622


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 2

    def which_method_to_test(self, which, x, y) -> int:
        """Decide which variation method to test"""
        s = Solution()
        t = Solution2()
        if which == 1:
            return s.build_tree_1(x, y)
        elif which == 2:
            return t.build_tree_2(x, y)

    def test_simple_example(self):
        """Testing binary tree example"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_1[0], TestCases.test_1[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_1[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on simple binary tree.",
            )

    def test_one_at_bottom_level(self):
        """Testing one leaf at bottom level"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_2[0], TestCases.test_2[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_2[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on one leaf at bottom level.",
            )

    def test_full_tree(self):
        """Testing full binary tree"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_3[0], TestCases.test_3[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_3[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on full binary tree.",
            )

    def test_all_left_children(self):
        """Testing all left children"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_4[0], TestCases.test_4[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_4[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on all left children.",
            )

    def test_all_right_children(self):
        """Testing all right children"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_5[0], TestCases.test_5[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_5[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on all right children.",
            )

    def test_one_node(self):
        """Testing one node in tree"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_6[0], TestCases.test_6[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_6[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on one node in tree.",
            )

    def test_two_nodes(self):
        """Testing two nodes in tree"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_7[0], TestCases.test_7[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertEqual(
                transformed_to_list,
                TestCases.test_7[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is incorrect on two nodes in tree.",
            )

    def test_incorrect(self):
        """Testing two nodes in tree"""
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(
                w, TestCases.test_8[0], TestCases.test_8[1]
            )
            transformed_to_list = display_tree_as_list(result)
            self.assertNotEqual(
                transformed_to_list,
                TestCases.test_8[2],
                "Which method: "
                + str(w)
                + " - "
                + "The result is correct when should be incorrect.",
            )


if __name__ == "__main__":
    unittest.main()
